import numpy as np
import cv2
import random

# Load the noisy video
noisy_video_path = 'myvideo.mp4'
cap = cv2.VideoCapture(noisy_video_path)

# Get video properties
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Define the objective function for GWO
def objective_function(params, noisy_frame):
    # Convert the frame to grayscale
    noisy_gray = cv2.cvtColor(noisy_frame, cv2.COLOR_BGR2GRAY)
    
    # Extract the denoising parameters from the params array
    h_color = int(params[0])
    h_space = int(params[1])

    # Apply noise removal algorithm using the parameters
    denoised_frame = cv2.fastNlMeansDenoisingColored(noisy_frame, None, h_color, h_space)

    # Calculate mean squared error between denoised frame and noisy frame
    mse = np.mean((denoised_frame - noisy_gray) ** 2)
    return mse

# Grey Wolf Optimizer implementation
def grey_wolf_optimizer(noisy_frame, max_iter=100, num_wolves=5, dim=2):
    # Define the parameter ranges based on your problem
    param_ranges = [(1, 100), (1, 100)]

    # Initialize the wolves with random parameter values
    wolves = np.random.uniform(low=param_ranges[0][0], high=param_ranges[0][1], size=(num_wolves, dim))

    # Initialize alpha, beta, and delta
    alpha = wolves[0]
    beta = wolves[1]
    delta = wolves[2]

    for iteration in range(max_iter):
        for i in range(num_wolves):
            fitness = objective_function(wolves[i], noisy_frame)
            alpha_fitness = objective_function(alpha, noisy_frame)
            beta_fitness = objective_function(beta, noisy_frame)
            delta_fitness = objective_function(delta, noisy_frame)

            if fitness < alpha_fitness:
                alpha = wolves[i]
            if alpha_fitness < fitness < beta_fitness:
                beta = wolves[i]
            if alpha_fitness < beta_fitness < fitness < delta_fitness:
                delta = wolves[i]

            a = 2 - iteration * (2 / max_iter)

            for j in range(dim):
                r1, r2 = random.random(), random.random()
                A1, C1 = 2 * a * r1 - a, 2 * r2
                D_alpha = abs(C1 * alpha[j] - wolves[i][j])
                wolves[i][j] = alpha[j] - A1 * D_alpha

        print(f"Iteration {iteration+1}/{max_iter} - Best MSE: {objective_function(alpha, noisy_frame)}")

    return alpha

# Create an output video writer
denoised_video_path = 'denoised_video.mp4'
out = cv2.VideoWriter(denoised_video_path, cv2.VideoWriter_fourcc(*'mp4v'), 30, (frame_width, frame_height))

# Process each frame of the noisy video
while True:
    ret, noisy_frame = cap.read()
    if not ret:
        break
    
    # Run GWO to find optimal denoising parameters
    best_params = grey_wolf_optimizer(noisy_frame)
    
    # Apply denoising using the best parameters to the current frame
    denoised_frame = cv2.fastNlMeansDenoisingColored(noisy_frame, None, int(best_params[0]), int(best_params[1]))
    
    # Write the denoised frame to the output video
    out.write(denoised_frame)

# Release the video capture and writer
cap.release()
out.release()

# Close all OpenCV windows
# cv2.destroyAllWindows()
