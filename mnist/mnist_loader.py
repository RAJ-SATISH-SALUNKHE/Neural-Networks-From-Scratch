import numpy as np

def load_mnist_images(filename):
    with open(filename, 'rb') as f:
        # Skip the magic number and dimensions (first 16 bytes)
        f.read(16)
        # Read the remaining bytes and reshape into a 28x28 array
        data = np.frombuffer(f.read(), dtype=np.uint8)
        return data.reshape(-1, 28, 28).astype(np.float32) / 255.0  # Normalize to [0, 1]

def load_mnist_labels(filename):
    with open(filename, 'rb') as f:
        # Skip the magic number (first 8 bytes)
        f.read(8)
        # Read the remaining bytes as labels
        return np.frombuffer(f.read(), dtype=np.uint8)

# Replace paths with the location of your extracted files
test_images = load_mnist_images('C:\\Users\\Raj.Salunkhe\\Desktop\\nn from scratch\\t10k-images.idx3-ubyte')
test_labels = load_mnist_labels('C:\\Users\\Raj.Salunkhe\\Desktop\\nn from scratch\\t10k-labels.idx1-ubyte')
train_images = load_mnist_images('C:\\Users\\Raj.Salunkhe\\Desktop\\nn from scratch\\train-images.idx3-ubyte')
train_labels = load_mnist_labels('C:\\Users\\Raj.Salunkhe\\Desktop\\nn from scratch\\train-labels.idx1-ubyte')

train_images = np.reshape(train_images, (train_images.shape[0], -1))  # Flatten each image to a 1D array
test_images = np.reshape(test_images, (test_images.shape[0], -1)) 

print(f"Train images shape: {train_images.shape}")
print(f"Train labels shape: {train_labels.shape}")
print(f"Test images shape: {test_images.shape}")
print(f"Test labels shape: {test_labels.shape}")
