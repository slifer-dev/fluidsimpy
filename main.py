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
