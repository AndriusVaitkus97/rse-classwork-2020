"""
A deliberately bad implementation of 
[Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.

This code simulates the swarming behaviour of bird-like objects ("boids").
"""
import numpy as np
from random import uniform

n_boids = 50

boids_x=[uniform(-450,50.0) for x in range(n_boids)]
boids_y=[uniform(300.0,600.0) for x in range(n_boids)]
boid_x_velocities=[uniform(0,10.0) for x in range(n_boids)]
boid_y_velocities=[uniform(-20.0,20.0) for x in range(n_boids)]

positions = np.array([[boids_x], [boids_y]]).reshape(50,2)
velocities = np.array([[boid_x_velocities], [boid_y_velocities]]).reshape(50,2)

def adjust_velocity(velocity, direction, increment):
    velocity += direction * increment
    return velocity


def update_boids(positions, velocities):
    n_positions = np.size(positions[1])
    print(n_positions)
    for i in range(n_positions):
        for j in range(n_positions):
            # Fly towards the middle
            velocities[i] = adjust_velocity(positions[j]-positions[i], velocities[i], 0.01/np.size(velocities[0]))
            # Fly away from nearby boids
            if (positions[j,0]-positions[i,0])**2 + (positions[j,0]-positions[i,0])**2 < 100:
                velocities[i] = adjust_velocity(positions[i]-positions[j], velocities[i], 1)
            # Try to match speed with nearby boids
            if (positions[j,0]-positions[i,0])**2 + (positions[j,0]-positions[i,0])**2 < 10000:
                velocities[i] = adjust_velocity(velocities[j]-velocities[i], velocities[i], 0.125/np.size(velocities[0]))
    # Move according to velocities
    for i in range(n_positions):
        positions[i] += velocities[i]