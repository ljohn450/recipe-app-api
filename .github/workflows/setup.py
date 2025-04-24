from setuptools import setup, find_packages

setup(
    name='recipe_app',  # Your project name
    version='0.1.0',  # Initial version
    author='Lavelle Denise Johnson',
    author_email='your.email@example.com',
    description='A simple Python app to manage and share recipes.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/recipe_app',
    packages=find_packages(),  # Automatically include all packages/modules
    include_package_data=True,
    install_requires=[
        'flask',          # If you're using Flask for a web UI
        'sqlalchemy',     # If you're using a database
        'requests',       # Example for making HTTP calls (if needed)
    ],
    entry_points={
        'console_scripts': [
            'recipe-app=recipe_app.cli:main',  # If you have a CLI interface
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Software Development :: Build Tools',
    ],
    python_requires='>=3.7',
)

