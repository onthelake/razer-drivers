"""
Mouse class
"""
from razer_daemon.hardware.device_base import RazerDeviceBrightnessSuspend as __RazerDeviceBrightnessSuspend, RazerDevice as __RazerDevice
from razer_daemon.misc.battery_notifier import BatteryManager as _BatteryManager
from razer_daemon.dbus_services.dbus_methods.deathadder_chroma import get_logo_brightness as _da_get_logo_brightness, set_logo_brightness as _da_set_logo_brightness, get_scroll_brightness as _da_get_scroll_brightness, set_scroll_brightness as _da_set_scroll_brightness, set_logo_active as _da_set_logo_active, set_scroll_active as _da_set_scroll_active


class RazerMambaChromaWireless(__RazerDeviceBrightnessSuspend):
    """
    Class for the Razer Mamba Chroma (Wireless)
    """
    USB_VID = 0x1532
    USB_PID = 0x0045
    HAS_MATRIX = True
    MATRIX_DIMS = [1, 15]  # 1 Row, 15 Cols
    METHODS = ['get_firmware', 'get_matrix_dims', 'has_matrix', 'get_device_name', 'get_device_type_mouse', 'get_brightness', 'set_brightness', 'get_battery', 'is_charging', 'set_wave_effect',
               'set_static_effect', 'set_spectrum_effect', 'set_reactive_effect', 'set_none_effect', 'set_breath_random_effect',
               'set_breath_single_effect', 'set_breath_dual_effect', 'set_custom_effect', 'set_key_row',
               'set_charge_effect', 'set_charge_colour', 'set_idle_time', 'set_low_battery_threshold', 'set_dpi_xy']

    def __init__(self, *args, **kwargs):
        super(RazerMambaChromaWireless, self).__init__(*args, **kwargs)

        self._battery_manager = _BatteryManager(self, self._device_number, 'Razer Mamba')

    def _close(self):
        """
        Close the key manager
        """
        super(RazerMambaChromaWireless, self)._close()

        self._battery_manager.close()


class RazerMambaChromaWired(__RazerDeviceBrightnessSuspend):
    """
    Class for the Razer Mamba Chroma (Wired)
    """
    USB_VID = 0x1532
    USB_PID = 0x0044
    HAS_MATRIX = True
    MATRIX_DIMS = [1, 15]  # 1 Row, 15 Cols
    METHODS = ['get_firmware', 'get_matrix_dims', 'has_matrix', 'get_device_name', 'get_device_type_mouse', 'get_brightness', 'set_brightness', 'set_wave_effect',
               'set_static_effect', 'set_spectrum_effect', 'set_reactive_effect', 'set_none_effect', 'set_breath_random_effect',
               'set_breath_single_effect', 'set_breath_dual_effect', 'set_custom_effect', 'set_key_row',
               'set_dpi_xy']

    def __init__(self, *args, **kwargs):
        super(RazerMambaChromaWired, self).__init__(*args, **kwargs)


class RazerMambaChromaTE(__RazerDeviceBrightnessSuspend):
    """
    Class for the Razer Mamba Chroma (Wired)
    """
    USB_VID = 0x1532
    USB_PID = 0x0046
    HAS_MATRIX = True
    MATRIX_DIMS = [1, 16]  # 1 Row, 16 Cols
    METHODS = ['get_firmware', 'get_matrix_dims', 'has_matrix', 'get_device_name', 'get_device_type_mouse', 'get_brightness', 'set_brightness', 'set_wave_effect',
               'set_static_effect', 'set_spectrum_effect', 'set_reactive_effect', 'set_none_effect', 'set_breath_random_effect',
               'set_breath_single_effect', 'set_breath_dual_effect', 'set_custom_effect', 'set_key_row',
               'set_dpi_xy']

    def __init__(self, *args, **kwargs):
        super(RazerMambaChromaTE, self).__init__(*args, **kwargs)


class RazerAbyssus(__RazerDevice):
    """
    Class for the Razer Abyssus
    """

    USB_VID = 0x1532
    USB_PID = 0x0042
    HAS_MATRIX = False
    MATRIX_DIMS = [-1, -1]  # 1 Row, 15 Cols
    METHODS = ['get_firmware', 'get_matrix_dims', 'has_matrix', 'get_device_name', 'get_device_type_mouse', 'set_logo_active', 'get_logo_active']

    def __init__(self, *args, **kwargs):
        super(RazerAbyssus, self).__init__(*args, **kwargs)

    def _resume_device(self):
        self.logger.debug("Abyssus doesnt have suspend/resume")

    def _suspend_device(self):
        self.logger.debug("Abyssus doesnt have suspend/resume")


class RazerImperiator(__RazerDevice):
    """
    Class for the Razer Imperiator 2012
    """

    USB_VID = 0x1532
    USB_PID = 0x002F
    HAS_MATRIX = False
    MATRIX_DIMS = [-1, -1]  # 1 Row, 15 Cols
    METHODS = ['get_firmware', 'get_matrix_dims', 'has_matrix', 'get_device_name', 'get_device_type_mouse', 'set_logo_active', 'get_logo_active', 'set_dpi_xy',
               'set_poll_rate', 'set_scroll_active', 'get_scroll_active']

    def __init__(self, *args, **kwargs):
        super(RazerImperiator, self).__init__(*args, **kwargs)

    def _resume_device(self):
        self.logger.debug("Imperiator doesnt have suspend/resume")

    def _suspend_device(self):
        self.logger.debug("Imperiator doesnt have suspend/resume")


class RazerOrochiWired(__RazerDeviceBrightnessSuspend):
    """
    Class for the Razer Mamba Chroma (Wireless)
    """
    USB_VID = 0x1532
    USB_PID = 0x0048
    HAS_MATRIX = False
    MATRIX_DIMS = [-1, -1]  # 1 Row, 15 Cols
    METHODS = ['get_firmware', 'get_matrix_dims', 'has_matrix', 'get_device_name', 'get_device_type_mouse', 'get_brightness', 'set_brightness',
               'set_static_effect', 'set_spectrum_effect', 'set_reactive_effect', 'set_none_effect', 'set_breath_random_effect',
               'set_breath_single_effect', 'set_breath_dual_effect', 'set_idle_time', 'set_low_battery_threshold', 'set_dpi_xy', 'set_scroll_active', 'get_scroll_active']


class RazerDeathadderChroma(__RazerDeviceBrightnessSuspend):
    """
    Class for the Razer Deathadder Chroma
    """
    USB_VID = 0x1532
    USB_PID = 0x0043
    HAS_MATRIX = False
    MATRIX_DIMS = [-1, -1]  # 1 Row, 15 Cols
    METHODS = ['get_firmware', 'get_matrix_dims', 'has_matrix', 'get_device_name', 'get_device_type_mouse',
               'set_logo_active', 'get_logo_active', 'get_logo_effect', 'get_logo_brightness', 'set_logo_brightness', 'set_logo_static', 'set_logo_pulsate', 'set_logo_blinking', 'set_logo_spectrum',
               'set_scroll_active', 'get_scroll_active', 'get_scroll_effect', 'get_scroll_brightness', 'set_scroll_brightness', 'set_scroll_static', 'set_scroll_pulsate', 'set_scroll_blinking', 'set_scroll_spectrum',
               'set_dpi_xy', 'set_poll_rate']

    def __init__(self, *args, **kwargs):
        super(RazerDeathadderChroma, self).__init__(*args, **kwargs)

        # Set brightness to max and LEDs to on, on startup
        _da_set_logo_brightness(self, 100)
        _da_set_scroll_brightness(self, 100)
        _da_set_logo_active(self, True)
        _da_set_scroll_active(self, True)


    def _suspend_device(self):
        """
        Suspend the device

        Get the current brightness level, store it for later and then set the brightness to 0
        """
        self.suspend_args.clear()
        self.suspend_args['brightness'] = (_da_get_logo_brightness(self), _da_get_scroll_brightness(self))

        # Todo make it context?
        self.disable_notify = True
        _da_set_logo_brightness(self, 0)
        _da_set_scroll_brightness(self, 0)
        self.disable_notify = False

    def _resume_device(self):
        """
        Resume the device

        Get the last known brightness and then set the brightness
        """
        logo_brightness = self.suspend_args.get('brightness', (100, 100))[0]
        scroll_brightness = self.suspend_args.get('brightness', (100, 100))[1]

        self.disable_notify = True
        _da_set_logo_brightness(self, logo_brightness)
        _da_set_scroll_brightness(self, scroll_brightness)
        self.disable_notify = False
