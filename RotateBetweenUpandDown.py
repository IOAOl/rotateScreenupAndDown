#!/usr/bin/env python
# coding: utf-8

# In[1]:


import win32api
import win32con


# In[5]:


device = win32api.EnumDisplayDevices(None,0);
dm = win32api.EnumDisplaySettings(device.DeviceName,win32con.ENUM_CURRENT_SETTINGS)
if dm.DisplayOrientation==win32con.DMDO_180:
    dm.DisplayOrientation = win32con.DMDO_DEFAULT
else:
    dm.DisplayOrientation = win32con.DMDO_180
win32api.ChangeDisplaySettingsEx(device.DeviceName,dm)


# In[ ]:




