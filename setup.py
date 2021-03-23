import setuptools

setuptools.setup(
    name="Houdini",
    version='1.0',
    py_modules=["houdini"],
    install_requires=[
        'Click',
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    entry_points='''
        [console_scripts]
        houdini=houdini:cli
    ''',
)
