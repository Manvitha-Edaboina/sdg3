import numpy as np
import tensorflow as tf

# Generator Model
def build_generator(latent_dim, output_shape):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(128, input_dim=latent_dim, activation='relu'),
        tf.keras.layers.Dense(256, activation='relu'),
        tf.keras.layers.Dense(output_shape, activation='sigmoid')
    ])
    return model

# Discriminator Model
def build_discriminator(input_shape):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(256, input_shape=(input_shape,), activation='relu'),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    return model

# GAN Model
def build_gan(generator, discriminator):
    discriminator.trainable = False
    model = tf.keras.Sequential()
    model.add(generator)
    model.add(discriminator)
    return model

# Generate random noise for input to the generator
def generate_noise(batch_size, latent_dim):
    return np.random.normal(0, 1, (batch_size, latent_dim))

# Generate synthetic data using the generator
def generate_synthetic_data(generator, num_samples, latent_dim):
    noise = generate_noise(num_samples, latent_dim)
    synthetic_data = generator.predict(noise)
    return synthetic_data

# Define GAN hyperparameters
latent_dim = 100
input_shape = 28*28  # Example: MNIST image size
batch_size = 64

# Build and compile the models
generator = build_generator(latent_dim, input_shape)
discriminator = build_discriminator(input_shape)
gan = build_gan(generator, discriminator)

gan.compile(loss='binary_crossentropy', optimizer='adam')
