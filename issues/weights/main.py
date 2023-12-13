from scipy import signal

a = [1, -0.5, 0.25]
b = [0.5, 1.25, 0.75]

# Get the impulse response of the filter
_, h = signal.impulse((b, a))

# Print the real impulse response
print("Impulse Response:", h.real)