from setuptools import setup, find_packages


setup(name="opcua2azure",
      version="0.1.0",
      description="OPC-UA to Azure IoT Hub",
      author="Olivier R-D, Andrew J",
      url='https://github.com/zeroentity/opcua-2-azure/',
      packages=["opcua2azure"],
      license="GNU General Public License",
      install_requires=["freeopcua"],
      entry_points={'console_scripts':
                    ['opcua2azure = opcua2azure.mainwindow:main']
                    }
      )
