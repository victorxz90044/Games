import win32com.client 
strComputer = "." 
objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator") 
objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2") 
colItems = objSWbemServices.ExecQuery("Select * from Win32_QuickFixEngineering") 
for objItem in colItems: 
    print( "Caption: ", objItem.Caption )
    print( "Description: ", objItem.Description )
    print( "Fix Comments: ", objItem.FixComments) 
    print( "HotFix ID: ", objItem.HotFixID )
    print( "Installed By: ", objItem.InstalledBy )
    print( "Installed On: ", objItem.InstalledOn) 
    print("\n")