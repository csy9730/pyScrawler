# Setting

配置规则：
按照优先级排序
1. cmdline
2. spider custom-setting
3. project-setting
4. default setting
5. global default setting

优先级从低到高排列
``` python
SETTINGS_PRIORITIES = {
    'default': 0,
    'command': 10,
    'project': 20,
    'cmdline': 40,
}
```