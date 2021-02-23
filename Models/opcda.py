#importing libraries
from template import OpenOPC
import operator
from Models.logs import operations
from datetime import datetime


#reading parameters
def Read_tags(json_data):
    logs = {}
    #accessing result class
    returnData = DATA_RESULT()
    returnData.error = False
    try:
        # validate json data
        if 'ipaddress' in json_data and 'server' in json_data and'group' in json_data and 'tags' in json_data:
            #accesing input json data
            assert json_data['ipaddress']!= ''
            ipaddress = json_data['ipaddress']
            assert json_data['server']!= ''
            server = json_data['server']
            assert json_data['group']!= ''
            group = json_data['group']
            assert json_data['tags']!= ''
            tags = json_data['tags']
        else:
            raise KeyError("Please check!,kindly input in proper json formatted")

        #validate input data
        returnData = ValidateData(ipaddress,tags)
        if returnData.error:
            #store logs into DB
            logs['CreateAt'] = datetime.now()
            logs['Error_Log'] = returnData.errormessage
            operations().insert_logs('OPCDA','Logs',logs)
            return returnData
        
        #connection
        opc=OpenOPC.open_client(ipaddress)
        opc.connect(server)

        #read tags
        values = opc.read(tags,group=group,update=1)   
        
        #connection close
        opc.remove(group)
        opc.close()
        
        result = []
        #result into dictionary
        for variable in values:
            parameter = {}
            parameter["parameter"] = variable[0]
        
            #validate parameter value
            if(type(variable[1]) == float):
                parameter["value"] = round(variable[1],3)
            else:
                parameter["value"] = variable[1]
            parameter["quality"] = variable[2]
            parameter["timestamp"] = variable[3]
            result.append(parameter)

        #return valid data
        returnData.data = result
        returnData.error = False
        returnData.errormessage = None
        return returnData
    except OpenOPC.TimeoutError:
        #return valid data
        returnData.data = None
        returnData.error = True
        returnData.errormessage = "TimeoutError occured"
        #store logs into DB
        logs['CreateAt'] = datetime.now()
        logs['Error_Log'] = returnData.errormessage
        operations().insert_logs('OPCDA','Logs',logs)
        return returnData
    except KeyError:
        #return valid data
        returnData.data = None
        returnData.error = True
        returnData.errormessage = "Please check!,kindly input in proper json formatted"
        #store logs into DB
        logs['CreateAt'] = datetime.now()
        logs['Error_Log'] = returnData.errormessage
        operations().insert_logs('OPCDA','Logs',logs)
        return returnData
    except AssertionError:
        #return valid data
        returnData.data = None
        returnData.error = True
        returnData.errormessage = "Kindly Check!, your json input values"
        #store logs into DB
        logs['CreateAt'] = datetime.now()
        logs['Error_Log'] = returnData.errormessage
        operations().insert_logs('OPCDA','Logs',logs)
        return returnData
    except UnboundLocalError:
        #return valid data
        returnData.data = None
        returnData.error = True
        returnData.errormessage = "Kindly Check!, your json input format"
        #store logs into DB
        logs['CreateAt'] = datetime.now()
        logs['Error_Log'] = returnData.errormessage
        operations().insert_logs('OPCDA','Logs',logs)
        return returnData

#reading parameters
def Write_SingleTag(json_data):
    logs = {}
    #accessing result class
    returnData = DATA_RESULT()
    returnData.error = True
    try:
        # validate json data
        if 'ipaddress' in json_data and 'server' in json_data and'tag' in json_data and 'value_to_write' in json_data:
            #accesing input json data
            assert json_data['ipaddress']!= ''
            ipaddress = json_data['ipaddress']
            assert json_data['server']!= ''
            server = json_data['server']
            assert json_data['tag']!= ''
            tag = json_data['tag']
            assert json_data['value_to_write']!= ''
            value = json_data['value_to_write']
        else:
            raise KeyError("Please check!,kindly input in proper json formatted")

        
        #validate input data
        returnData = ValidateData(ipaddress,tag)
        if returnData.error:
            #store logs into DB
            logs['CreateAt'] = datetime.now()
            logs['Error_Log'] = returnData.errormessage
            operations().insert_logs('OPCDA','Logs',logs)
            return returnData

        #connection
        opc=OpenOPC.open_client(ipaddress)
        opc.connect(server)


        #read tags
        values = opc.write((str(tag),value),include_error = True)
        
        #validate result
        if values[0] == "Error":
            #store logs into DB
            logs['CreateAt'] = datetime.now()
            logs['Error_Log'] = values[1]
            operations().insert_logs('OPCDA','Logs',logs)

        #connection close
        opc.close()

        result = []
        #result into dictionary
        parameter = {}
        parameter["parameter"] = tag
        parameter["Write_Result"] = values[0]
        parameter["Description"] = values[1]
        result.append(parameter)

        #return valid data
        returnData.data = result
        returnData.error = False
        returnData.errormessage = None
        return returnData
    except OpenOPC.TimeoutError:
        #return valid data
        returnData.data = None
        returnData.error = True
        returnData.errormessage = "TimeoutError occured"
        #store logs into DB
        logs['CreateAt'] = datetime.now()
        logs['Error_Log'] = returnData.errormessage
        operations().insert_logs('OPCDA','Logs',logs)
        return returnData
    except KeyError:
        #return valid data
        returnData.data = None
        returnData.error = True
        returnData.errormessage = "Please check!,kindly input in proper json formatted"
        #store logs into DB
        logs['CreateAt'] = datetime.now()
        logs['Error_Log'] = returnData.errormessage
        operations().insert_logs('OPCDA','Logs',logs)
        return returnData
    except AssertionError:
        #return valid data
        returnData.data = None
        returnData.error = True
        returnData.errormessage = "Kindly Check!, your json input values"
        #store logs into DB
        logs['CreateAt'] = datetime.now()
        logs['Error_Log'] = returnData.errormessage
        operations().insert_logs('OPCDA','Logs',logs)
        return returnData
    except UnboundLocalError:
        #return valid data
        returnData.data = None
        returnData.error = True
        returnData.errormessage = "Kindly Check!, your json input format"
        #store logs into DB
        logs['CreateAt'] = datetime.now()
        logs['Error_Log'] = returnData.errormessage
        operations().insert_logs('OPCDA','Logs',logs)
        return returnData


#reading parameters
def Write_MultipleTag(json_data):
    logs = {}
    #accessing result class
    returnData = DATA_RESULT()
    returnData.error = True

    try:
        # validate json data
        if 'ipaddress' in json_data and 'server' in json_data and'tags' in json_data and 'values_to_write' in json_data:
            #accesing input json data
            assert json_data['ipaddress']!= ''
            ipaddress = json_data['ipaddress']
            assert json_data['server']!= ''
            server = json_data['server']
            assert json_data['tags']!= ''
            tags = json_data['tags']
            assert json_data['values_to_write']!= ''
            values = json_data['values_to_write']
        else:
            raise KeyError("Please check!,kindly input in proper json formatted")

        #validate input data
        returnData = ValidateData(ipaddress,tags)
        if returnData.error:
            #store logs into DB
            logs['CreateAt'] = datetime.now()
            logs['Error_Log'] = returnData.errormessage
            operations().insert_logs('OPCDA','Logs',logs)
            return returnData

        #connection
        opc=OpenOPC.open_client(ipaddress)
        opc.connect(server)

        zip_data = zip(tags,values)
        #read tags
        values = opc.write(list(zip_data),include_error = True)
        
        #connection close
        opc.close()

        result = []
        
        #result into dictionary
        for item in values:
            parameter = {}
            parameter["parameter"] = item[0]
            parameter["Write_Result"] = item[1]
            parameter["Description"] = item[2]
            result.append(parameter)

        #return valid data
        returnData.data = result
        returnData.error = False
        returnData.errormessage = None
        return returnData
    except OpenOPC.TimeoutError:
        #return valid data
        returnData.data = None
        returnData.error = True
        returnData.errormessage = "TimeoutError occured"
        #store logs into DB
        logs['CreateAt'] = datetime.now()
        logs['Error_Log'] = returnData.errormessage
        operations().insert_logs('OPCDA','Logs',logs)
        return returnData
    except KeyError:
        #return valid data
        returnData.data = None
        returnData.error = True
        returnData.errormessage = "Please check!,kindly input in proper json formatted"
        #store logs into DB
        logs['CreateAt'] = datetime.now()
        logs['Error_Log'] = returnData.errormessage
        operations().insert_logs('OPCDA','Logs',logs)
        return returnData
    except AssertionError:
        #return valid data
        returnData.data = None
        returnData.error = True
        returnData.errormessage = "Kindly Check!, your json input values"
        #store logs into DB
        logs['CreateAt'] = datetime.now()
        logs['Error_Log'] = returnData.errormessage
        operations().insert_logs('OPCDA','Logs',logs)
        return returnData
    except UnboundLocalError:
        #return valid data
        returnData.data = None
        returnData.error = True
        returnData.errormessage = "Kindly Check!, your json input format"
        #store logs into DB
        logs['CreateAt'] = datetime.now()
        logs['Error_Log'] = returnData.errormessage
        operations().insert_logs('OPCDA','Logs',logs)
        return returnData



#validating json information
def ValidateData(ipaddress, parameters):
    #accessing result class
    returnData = DATA_RESULT()
    returnData.error = False

    #validate ip
    if ipaddress != None and ipaddress != '':
        #convert each ip segment into int array
        ipSegment = [int(x) for x in str(ipaddress).split('.')]

        if len(ipSegment) != 4:
            returnData.error = True
            returnData.errormessage = 'Invalid IP Address'
            return returnData


        for ips in  ipSegment:
            if ips < 0 or ips >255:
                returnData.error = True
                returnData.errormessage = 'Invalid IP Numbers'
                return returnData


    #validate parameters:
    if type(parameters) != list:
        if type(parameters) == unicode:
            returnData.error = False
            returnData.errormessage = None
        else:
            returnData.error = True
            returnData.errormessage = 'Parameters should be on List'
            return returnData


    #return validation ok
    return returnData



#Data result
class DATA_RESULT():
    data = None
    error = True
    errormessage = None