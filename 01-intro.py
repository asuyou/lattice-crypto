import numpy as np

# Constants
q = 655_360_001
n = 1_000
N = 500

noise = np.matrix(
    np.random.randint(low=0, high=q, size=[1, N])
)

t = np.matrix(
    np.random.randint(low=0, high=q, size=[n,1])
)

# [1, ...other vals]
secret_key = np.insert(t, 0, 1)

A = np.random.randint(low=0, high=q, size=[n, N])

b = (A.T * t).T + noise
b = b % q

# Public Key fields
pub_key = np.hstack((b.T, -A.T))
print(f"Key Shape: {pub_key.shape}")

message = np.random.randint(0, 2)
m_vec = np.insert(np.zeros(n), 0, message)
r = np.random.randint(low=0, high=2, size=[N, 1])

chiper = (pub_key.T * r).T + ((q//2) * m_vec) % q

# Decryption
temp = (2/q) * (np.dot(chiper, secret_key.T) % q)
decoded_msg = temp.round() % 2

print(f"Original: {message}\nDecoded: {decoded_msg}\nValid: {decoded_msg == message}")

