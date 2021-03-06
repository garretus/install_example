from distutils.core import setup

#This is a list of files to install, and where
#(relative to the 'root' dir, where setup.py is)
#You could be more specific.
files = ["config/*"]

setup(name = "install_example",
    version = "0.0.2",
    description = "yadda yadda",
    author = "@Garretus",
    author_email = "email@someplace.com",
    url = "whatever",
    #Name the folder where your packages live:
    #(If you have other packages (dirs) or modules (py files) then
    #put them into the package directory - they will be found 
    #recursively.)
    packages = ['install_example'],

    #'package' package must contain files (see list above)
    #I called the package 'package' thus cleverly confusing the whole issue...
    #This dict maps the package name =to=> directories
    #It says, package *needs* these files.
    package_data = {'install_example' : files },

    #'runner' is in the root.
    scripts = ["install_example_runner"],
    long_description = """Really long text here.""" ,
    #
    #This next part it for the Cheese Shop, look a little down the page.
    classifiers=[
         'Development Status :: 4 - Beta',
         'Environment :: X11 Applications :: GTK',
         'Intended Audience :: End Users/Desktop',
         'Intended Audience :: Developers',
         'License :: OSI Approved :: GNU General Public License (GPL)',
         'Operating System :: POSIX :: Linux',
         'Programming Language :: Python',
         'Topic :: Desktop Environment',
         'Topic :: Text Processing :: Fonts'
     ]
) 