"""
The scenario involves a domain filled with a fluid that adheres the Navier-Stokes equations for incompressible fluids,
hot smoke is immersed in this fluid, which follows an advection equation driven by the fluid velocity field.
smoke is emitted from a circular-shaped emitter and applies a buoyant force on the momentum equation relative to the fluid.

The domain that we are dealing with is a closed box with solid boundaries.

The interested Navier-Stokes equation is the one that follows:

Momentum:   ∂u/∂t + (u ⋅ ∇)u = -1/ρ ∇p + v∇²u + f

Together with the incompressibility constraint

Incompressibility:  ∇ ⋅ u = 0

The advection equation that needs to follow the smoke is the following:

Advection:  ∂s/∂t + ∇ ⋅ (u ⋅ s) = a∇²s + i

Terms in the expressions:
u: 2d velocity field

p: pressure
f: external foces to the fluid mass, in this case the external force applied to the fluid is the bouyancy caused by the hot smoke
v: kinematic viscosity
ρ: density
t: time
∇: nabla operator
∇²: laplacian operator
s: scalar field that represents the concentration of the smoke
a: diffusivity if the smoke in the fluid
i: inflow of smoke in the domain
"""

from phi import flow
import matplotlib.pyplot as plt

STEPS = 200


def main() -> None:
    
    def calculate_next_state(previous_velocity, previous_smoke, dt=1.0) -> tuple[flow.StaggeredGrid, flow.CenteredGrid]:
        next_smoke = flow.advect.mac_cormack(previous_smoke, previous_velocity, dt) + inflow_field
        bouyancy_force = next_smoke * (0.0, 0.1) @ previous_velocity
        not_zero_div_velocity = flow.advect.semi_lagrangian(previous_velocity, previous_velocity, dt) + bouyancy_force * dt
        next_velocity, _ = flow.fluid.make_incompressible(not_zero_div_velocity)
        return next_velocity, next_smoke
        
        
        
    domain = flow.Box(x = 128, y = 128)
    
    velocity_field = flow.StaggeredGrid(
        values = (0.0, 0.0),
        extrapolation = 0.0
        x = 64,
        y = 64,
        bounds = domain
    )
    
    smoke_field = flow.CenteredGrid(
        values = 0.0
        extrapolation = flow.extrapolation.BOUNDARY,
        x = 256,
        y = 256,
        bounds = domain
    )
    
    inflow_field = flow.CenteredGrid(
        values = flow.SoftGeometryMask(
            flow.Sphere(
                x = 48,
                y = 8,
                radius = 16
            )
        ),
        extrapolation = 0,
        bounds = smoke_field.bounds
        resolution = smoke_field.resolution
        
    )
    
if __name__ == '__main__':
    main()
    