## *********************************************************
##
## File autogenerated for the chapter2_tutorials package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 245, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [], 'parameters': [{'srcline': 292, 'description': 'A double parameter', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'double_param', 'edit_method': '', 'default': 0.1, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 292, 'description': 'A string parameter', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'str_param', 'edit_method': '', 'default': 'Chapter2_dynamic_reconfigure', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 292, 'description': 'An Integer parameter', 'max': 100, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'int_param', 'edit_method': '', 'default': 1, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 292, 'description': 'A Boolean parameter', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'bool_param', 'edit_method': '', 'default': True, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 292, 'description': 'Select from the list', 'max': 3, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'size', 'edit_method': "{'enum_description': 'Select from the list', 'enum': [{'srcline': 13, 'description': 'Low is 0', 'srcfile': '/home/max/catkin_ws/src/chapter2_tutorials/cfg/chapter2.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'Low'}, {'srcline': 14, 'description': 'Medium is 1', 'srcfile': '/home/max/catkin_ws/src/chapter2_tutorials/cfg/chapter2.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'Medium'}, {'srcline': 15, 'description': 'High is 2', 'srcfile': '/home/max/catkin_ws/src/chapter2_tutorials/cfg/chapter2.cfg', 'cconsttype': 'const int', 'value': 2, 'ctype': 'int', 'type': 'int', 'name': 'High'}]}", 'default': 1, 'level': 0, 'min': 0, 'type': 'int'}], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

chapter2__Low = 0
chapter2__Medium = 1
chapter2__High = 2
