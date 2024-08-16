from setuptools import setup, find_packages
print(find_packages())
with open("requirements.txt", "r", encoding='utf8') as f:
    install_requires = f.readlines()
    
setup(
    name="robo-trader",
    version="0.1.0",
    description="Robo Trading Platform for learning purposes",
    author="Jan Matter",
    author_email="jan.matter@outlook.com",
    packages=find_packages(),
    install_requires=install_requires
)