Installaion steps:
1. Windows PC (for OPC gateway service)
    
    1. Download and install python 32bit from the below link
        https://www.python.org/downloads/windows/
    
    2. install pywin32 which matches to your python version 32bit from the below link 
        https://github.com/mhammond/pywin32/releases 
    
    3. install pyro pip install Pyro4 
    
    4. Make sure these environment variables in your Windows box are set as shown:

        OPC_CLASS=Matrikon.OPC.Automation;Graybox.OPC.DAWrapper;HSCOPC.Automation;RSI.OPCAutomation;OPC.Automation
        OPC_CLIENT=OpenOPC
        OPC_GATE_HOST=192.168.1.96    # IMPORTANT: Replace with your IP address
        OPC_GATE_PORT=7766
        OPC_HOST=localhost
        OPC_MODE=dcom
        OPC_SERVER=Hci.TPNServer;HwHsc.OPCServer;opc.deltav.1;AIM.OPC.1;Yokogawa.ExaopcDAEXQ.1;OSI.DA.1;OPC.PHDServerDA.1;Aspen.Infoplus21_DA.1;National Instruments.OPCLabVIEW;RSLinx OPC Server;KEPware.KEPServerEx.V4;Matrikon.OPC.Simulation;Prosys.OPC.Simulation

        If they are not set, open a command prompt window to do that by typing:
        C:\>set OPC_GATE_HOST=172.16.4.22    # this is an example
    
    5. Install the OpenOPC Gateway Service 
        1. Download OpenOPC from the below link
            https://github.com/joseamaita/openopc120.git
        2. Extract the compressed file to a folder in your Windows box (i.e. C:\OpenOPC37).
        3. Open a command prompt window (run it as administrator) and go to your work directory (i.e. C:\OpenOPC37).
        4. Change to the lib folder.
        5. Register the OPC automation wrapper ( gbda_aut.dll ) by typing this in the command line:
            C:\OpenOPC37\lib>regsvr32 gbda_aut.dll
        6. If, for any reason, you want to uninstall this file and remove it from your system registry later, type this in the command line:
            C:\OpenOPC37\lib>regsvr32 gbda_aut.dll -u
    
    6. Install the OpenOPC Gateway Service
        This goal can be achieved by running the "OpenOPCService.py" script with the Python interpreter and the "install" argument (remember to do it as administrator):

        1. In the command prompt window, go to your work directory (i.e. C:\OpenOPC37).
        2. Change to the src folder.
        3 Install the OpenOPC Gateway Service by typing this in the command line:
            C:\OpenOPC37\src>python OpenOPCService.py install
        4. Wait while the following message is shown on the screen:
            Installing service zzzOpenOPCService
            Service installed
    7. Usage
        
        1. Start the OpenOPC Gateway Service
            This task can be completed from one of two ways (make sure to have it installed first):

            1. By clicking the Start link on the "OpenOPC Gateway Service" from the "Services" window (Start -> Control Panel -> System and Security -> Administrative Tools).
            2. By running the net start SERVICE command like this:
                C:\OpenOPC37\bin>net start zzzOpenOPCService
            3. If you have problems starting the service, you can also try to start this in "debug" mode:
                C:\OpenOPC37\src>python OpenOPCService.py debug
        
        2. Stop the OpenOPC Gateway Service
            This task can be completed from one of two ways:

            1. By clicking the Stop link on the "OpenOPC Gateway Service" from the "Services" window (Stop -> Control Panel -> System and Security -> Administrative Tools).
            2. By running the net stop SERVICE command like this:
                C:\OpenOPC37\bin>net stop zzzOpenOPCService
        
        3. Configure the way the OpenOPC Gateway Service starts
            If you are going to use this service frequently, it would be better to configure it to start in "automatic" mode. To do this:

            1. Select the "OpenOPC Gateway Service" from the "Services" window.
            2. Right-click and choose "Properties".
            3. Change the startup mode to "Automatic". Click "Apply" and "OK" buttons.
            4. Start the service (if not already started).
    
    8. That's it all the required libraries has been installed to run required OPc gateway service.

2. Linux PC 
    1. install docker 
    2. Install docker compose
    3. goto the library where your python program is available 
    4. Run app run command docker-compose up --build -d