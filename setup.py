from setuptools import setup, find_packages

setup(
    name='latent-diffusion',
    version='2024.5.16',
    description='',
    packages=find_packages(),
    install_requires=[
        'torch',
        'numpy',
        'tqdm',
    ],
)
