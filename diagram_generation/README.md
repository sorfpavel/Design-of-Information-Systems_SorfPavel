# Class diagram generation

One option is pyreverse (part of pylint):

> pip install pylint

If the pyreverse is in your system path, you can run it as:

> pyreverse -o png <path_to_src>

In case you use windows and you do not want to add it to the system path,
you can find the exact location of pyreverse exe and run it directly.
See example:

> C:\Users\matou\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\Scripts\pyreverse -o png <path_to_src>
