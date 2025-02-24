import json
import os
import time

import serial
import wx


class Frame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(
            parent=None,
            title=title,
            style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX),
            size=wx.Size(268, 655),
        )
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_panel = wx.Panel(self)
        panel_sizer = wx.BoxSizer(wx.VERTICAL)
        buttons_sizer_1 = wx.GridBagSizer(hgap=2, vgap=2)
        buttons_sizer_2 = wx.GridBagSizer(hgap=2, vgap=2)
        buttons_sizer_3 = wx.GridBagSizer(hgap=2, vgap=2)
        buttons_sizer_4 = wx.GridBagSizer(hgap=2, vgap=2)
        buttons_sizer_5 = wx.BoxSizer(wx.VERTICAL)

        if os.path.exists("config.json"):
            with open("config.json", "r") as f:
                self.config = json.load(f)
                try:
                    self.config["port"] = str(self.config["port"])
                except (ValueError, KeyError):
                    self.config["port"] = ""
        else:
            self.config = {"port": ""}

        self.com_port_label = wx.StaticText(main_panel, label="Port")
        self.com_port = wx.TextCtrl(main_panel, value=self.config["port"])
        com_port_sizer = wx.GridBagSizer(hgap=15)
        com_port_sizer.Add(
            self.com_port_label,
            wx.GBPosition(0, 0),
            flag=wx.EXPAND | wx.ALIGN_CENTRE_VERTICAL,
        )
        com_port_sizer.Add(
            self.com_port,
            wx.GBPosition(0, 1),
            flag=wx.EXPAND | wx.ALIGN_CENTRE_VERTICAL,
        )

        self.pwr_on_btn = wx.Button(main_panel, label="PWR ON", size=wx.Size(120, 23))
        self.pwr_on_btn.Bind(wx.EVT_BUTTON, self.on_pwr_on_button)
        self.pwr_off_btn = wx.Button(main_panel, label="PWR OFF", size=wx.Size(120, 23))
        self.pwr_off_btn.Bind(wx.EVT_BUTTON, self.on_pwr_off_button)

        self.input_btn = wx.Button(main_panel, label="INPUT", size=wx.Size(79, 23))
        self.input_btn.Bind(wx.EVT_BUTTON, self.on_input_button)
        self.out_btn = wx.Button(main_panel, label="OUT", size=wx.Size(80, 23))
        self.out_btn.Bind(wx.EVT_BUTTON, self.on_out_button)
        self.scl_btn = wx.Button(main_panel, label="SCL", size=wx.Size(79, 23))
        self.scl_btn.Bind(wx.EVT_BUTTON, self.on_scl_button)
        self.sfx_btn = wx.Button(main_panel, label="SFX", size=wx.Size(79, 23))
        self.sfx_btn.Bind(wx.EVT_BUTTON, self.on_sfx_button)
        self.adc_btn = wx.Button(main_panel, label="ADC", size=wx.Size(80, 23))
        self.adc_btn.Bind(wx.EVT_BUTTON, self.on_adc_button)
        self.prof_btn = wx.Button(main_panel, label="PROF", size=wx.Size(79, 23))
        self.prof_btn.Bind(wx.EVT_BUTTON, self.on_prof_button)
        self.num1_btn = wx.Button(main_panel, label="1", size=wx.Size(79, 23))
        self.num1_btn.Bind(wx.EVT_BUTTON, self.on_num1_button)
        self.num2_btn = wx.Button(main_panel, label="2", size=wx.Size(80, 23))
        self.num2_btn.Bind(wx.EVT_BUTTON, self.on_num2_button)
        self.num3_btn = wx.Button(main_panel, label="3", size=wx.Size(79, 23))
        self.num3_btn.Bind(wx.EVT_BUTTON, self.on_num3_button)
        self.num4_btn = wx.Button(main_panel, label="4", size=wx.Size(79, 23))
        self.num4_btn.Bind(wx.EVT_BUTTON, self.on_num4_button)
        self.num5_btn = wx.Button(main_panel, label="5", size=wx.Size(80, 23))
        self.num5_btn.Bind(wx.EVT_BUTTON, self.on_num5_button)
        self.num6_btn = wx.Button(main_panel, label="6", size=wx.Size(79, 23))
        self.num6_btn.Bind(wx.EVT_BUTTON, self.on_num6_button)
        self.num7_btn = wx.Button(main_panel, label="7", size=wx.Size(79, 23))
        self.num7_btn.Bind(wx.EVT_BUTTON, self.on_num7_button)
        self.num8_btn = wx.Button(main_panel, label="8", size=wx.Size(80, 23))
        self.num8_btn.Bind(wx.EVT_BUTTON, self.on_num8_button)
        self.num9_btn = wx.Button(main_panel, label="9", size=wx.Size(79, 23))
        self.num9_btn.Bind(wx.EVT_BUTTON, self.on_num9_button)
        self.num10_btn = wx.Button(main_panel, label="10", size=wx.Size(79, 23))
        self.num10_btn.Bind(wx.EVT_BUTTON, self.on_num10_button)
        self.num11_btn = wx.Button(main_panel, label="11", size=wx.Size(80, 23))
        self.num11_btn.Bind(wx.EVT_BUTTON, self.on_num11_button)
        self.num12_btn = wx.Button(main_panel, label="12", size=wx.Size(79, 23))
        self.num12_btn.Bind(wx.EVT_BUTTON, self.on_num12_button)

        self.menu_btn = wx.Button(main_panel, label="MENU", size=wx.Size(79, 23))
        self.menu_btn.Bind(wx.EVT_BUTTON, self.on_menu_button)
        self.up_btn = wx.Button(main_panel, label="↑", size=wx.Size(80, 23))
        self.up_btn.Bind(wx.EVT_BUTTON, self.on_up_button)
        self.back_btn = wx.Button(main_panel, label="BACK", size=wx.Size(79, 23))
        self.back_btn.Bind(wx.EVT_BUTTON, self.on_back_button)
        self.left_btn = wx.Button(main_panel, label="←", size=wx.Size(79, 23))
        self.left_btn.Bind(wx.EVT_BUTTON, self.on_left_button)
        self.ok_btn = wx.Button(main_panel, label="ENTER", size=wx.Size(80, 23))
        self.ok_btn.Bind(wx.EVT_BUTTON, self.on_ok_button)
        self.right_btn = wx.Button(main_panel, label="→", size=wx.Size(79, 23))
        self.right_btn.Bind(wx.EVT_BUTTON, self.on_right_button)
        self.diag_btn = wx.Button(main_panel, label="DIAG", size=wx.Size(79, 23))
        self.diag_btn.Bind(wx.EVT_BUTTON, self.on_diag_button)
        self.down_btn = wx.Button(main_panel, label="↓", size=wx.Size(79, 23))
        self.down_btn.Bind(wx.EVT_BUTTON, self.on_down_button)
        self.stat_btn = wx.Button(main_panel, label="STAT", size=wx.Size(79, 23))
        self.stat_btn.Bind(wx.EVT_BUTTON, self.on_stat_button)

        self.gain_btn = wx.Button(main_panel, label="A. GAIN", size=wx.Size(79, 23))
        self.gain_btn.Bind(wx.EVT_BUTTON, self.on_gain_button)
        self.pause_btn = wx.Button(main_panel, label="PAUSE", size=wx.Size(80, 23))
        self.pause_btn.Bind(wx.EVT_BUTTON, self.on_pause_button)
        self.gen_btn = wx.Button(main_panel, label="GENLOCK", size=wx.Size(79, 23))
        self.gen_btn.Bind(wx.EVT_BUTTON, self.on_gen_button)
        self.phase_btn = wx.Button(main_panel, label="A. PHASE", size=wx.Size(79, 23))
        self.phase_btn.Bind(wx.EVT_BUTTON, self.on_phase_button)
        self.safe_btn = wx.Button(main_panel, label="SAFE", size=wx.Size(80, 23))
        self.safe_btn.Bind(wx.EVT_BUTTON, self.on_safe_button)
        self.buffer_btn = wx.Button(main_panel, label="T. BUFFER", size=wx.Size(79, 23))
        self.buffer_btn.Bind(wx.EVT_BUTTON, self.on_buffer_button)
        self.res4k_btn = wx.Button(main_panel, label="4K", size=wx.Size(59, 23))
        self.res4k_btn.Bind(wx.EVT_BUTTON, self.on_res4k_button)
        self.res1080p_btn = wx.Button(main_panel, label="1080p", size=wx.Size(59, 23))
        self.res1080p_btn.Bind(wx.EVT_BUTTON, self.on_res1080p_button)
        self.res1440p_btn = wx.Button(main_panel, label="1440p", size=wx.Size(59, 23))
        self.res1440p_btn.Bind(wx.EVT_BUTTON, self.on_res1440p_button)
        self.res480p_btn = wx.Button(main_panel, label="480p", size=wx.Size(59, 23))
        self.res480p_btn.Bind(wx.EVT_BUTTON, self.on_res480p_button)
        self.res1_btn = wx.Button(main_panel, label="RES1", size=wx.Size(59, 23))
        self.res1_btn.Bind(wx.EVT_BUTTON, self.on_res1_button)
        self.res2_btn = wx.Button(main_panel, label="RES2", size=wx.Size(59, 23))
        self.res2_btn.Bind(wx.EVT_BUTTON, self.on_res2_button)
        self.res3_btn = wx.Button(main_panel, label="RES3", size=wx.Size(59, 23))
        self.res3_btn.Bind(wx.EVT_BUTTON, self.on_res3_button)
        self.res4_btn = wx.Button(main_panel, label="RES4", size=wx.Size(59, 23))
        self.res4_btn.Bind(wx.EVT_BUTTON, self.on_res4_button)
        self.aux1_btn = wx.Button(main_panel, label="AUX1", size=wx.Size(59, 23))
        self.aux1_btn.Bind(wx.EVT_BUTTON, self.on_aux1_button)
        self.aux2_btn = wx.Button(main_panel, label="AUX2", size=wx.Size(59, 23))
        self.aux2_btn.Bind(wx.EVT_BUTTON, self.on_aux2_button)
        self.aux3_btn = wx.Button(main_panel, label="AUX3", size=wx.Size(59, 23))
        self.aux3_btn.Bind(wx.EVT_BUTTON, self.on_aux3_button)
        self.aux4_btn = wx.Button(main_panel, label="AUX4", size=wx.Size(59, 23))
        self.aux4_btn.Bind(wx.EVT_BUTTON, self.on_aux4_button)
        self.aux5_btn = wx.Button(main_panel, label="AUX5", size=wx.Size(59, 23))
        self.aux5_btn.Bind(wx.EVT_BUTTON, self.on_aux5_button)
        self.aux6_btn = wx.Button(main_panel, label="AUX6", size=wx.Size(59, 23))
        self.aux6_btn.Bind(wx.EVT_BUTTON, self.on_aux6_button)
        self.aux7_btn = wx.Button(main_panel, label="AUX7", size=wx.Size(59, 23))
        self.aux7_btn.Bind(wx.EVT_BUTTON, self.on_aux7_button)
        self.aux8_btn = wx.Button(main_panel, label="AUX8", size=wx.Size(59, 23))
        self.aux8_btn.Bind(wx.EVT_BUTTON, self.on_aux8_button)

        self.custom_btn = wx.Button(
            main_panel, label="Custom Command...", size=wx.Size(242, 23)
        )
        self.custom_btn.Bind(wx.EVT_BUTTON, self.on_custom_button)

        self.always_on_top_switch = wx.CheckBox(main_panel, label="Always On Top")
        self.always_on_top_switch.Bind(wx.EVT_CHECKBOX, self.on_always_on_top)

        buttons_sizer_1.Add(self.pwr_on_btn, wx.GBPosition(0, 0))
        buttons_sizer_1.Add(self.pwr_off_btn, wx.GBPosition(0, 1))

        buttons_sizer_2.Add(self.input_btn, wx.GBPosition(0, 0))
        buttons_sizer_2.Add(self.out_btn, wx.GBPosition(0, 1))
        buttons_sizer_2.Add(self.scl_btn, wx.GBPosition(0, 2))
        buttons_sizer_2.Add(self.sfx_btn, wx.GBPosition(1, 0))
        buttons_sizer_2.Add(self.adc_btn, wx.GBPosition(1, 1))
        buttons_sizer_2.Add(self.prof_btn, wx.GBPosition(1, 2))
        buttons_sizer_2.SetEmptyCellSize(wx.Size(1, 5))
        buttons_sizer_2.Add(self.num1_btn, wx.GBPosition(3, 0))
        buttons_sizer_2.Add(self.num2_btn, wx.GBPosition(3, 1))
        buttons_sizer_2.Add(self.num3_btn, wx.GBPosition(3, 2))
        buttons_sizer_2.Add(self.num4_btn, wx.GBPosition(4, 0))
        buttons_sizer_2.Add(self.num5_btn, wx.GBPosition(4, 1))
        buttons_sizer_2.Add(self.num6_btn, wx.GBPosition(4, 2))
        buttons_sizer_2.Add(self.num7_btn, wx.GBPosition(5, 0))
        buttons_sizer_2.Add(self.num8_btn, wx.GBPosition(5, 1))
        buttons_sizer_2.Add(self.num9_btn, wx.GBPosition(5, 2))
        buttons_sizer_2.Add(self.num10_btn, wx.GBPosition(6, 0))
        buttons_sizer_2.Add(self.num11_btn, wx.GBPosition(6, 1))
        buttons_sizer_2.Add(self.num12_btn, wx.GBPosition(6, 2))

        buttons_sizer_3.Add(self.menu_btn, wx.GBPosition(0, 0))
        buttons_sizer_3.Add(self.up_btn, wx.GBPosition(0, 1))
        buttons_sizer_3.Add(self.back_btn, wx.GBPosition(0, 2))
        buttons_sizer_3.Add(self.left_btn, wx.GBPosition(1, 0))
        buttons_sizer_3.Add(self.ok_btn, wx.GBPosition(1, 1))
        buttons_sizer_3.Add(self.right_btn, wx.GBPosition(1, 2))
        buttons_sizer_3.Add(self.diag_btn, wx.GBPosition(2, 0))
        buttons_sizer_3.Add(self.down_btn, wx.GBPosition(2, 1))
        buttons_sizer_3.Add(self.stat_btn, wx.GBPosition(2, 2))
        buttons_sizer_3.SetEmptyCellSize(wx.Size(1, 8))
        buttons_sizer_3.Add(self.gain_btn, wx.GBPosition(4, 0))
        buttons_sizer_3.Add(self.pause_btn, wx.GBPosition(4, 1))
        buttons_sizer_3.Add(self.gen_btn, wx.GBPosition(4, 2))
        buttons_sizer_3.Add(self.phase_btn, wx.GBPosition(5, 0))
        buttons_sizer_3.Add(self.safe_btn, wx.GBPosition(5, 1))
        buttons_sizer_3.Add(self.buffer_btn, wx.GBPosition(5, 2))

        buttons_sizer_4.Add(self.res4k_btn, wx.GBPosition(0, 0))
        buttons_sizer_4.Add(self.res1080p_btn, wx.GBPosition(0, 1))
        buttons_sizer_4.Add(self.res1440p_btn, wx.GBPosition(0, 2))
        buttons_sizer_4.Add(self.res480p_btn, wx.GBPosition(0, 3))
        buttons_sizer_4.Add(self.res1_btn, wx.GBPosition(1, 0))
        buttons_sizer_4.Add(self.res2_btn, wx.GBPosition(1, 1))
        buttons_sizer_4.Add(self.res3_btn, wx.GBPosition(1, 2))
        buttons_sizer_4.Add(self.res4_btn, wx.GBPosition(1, 3))
        buttons_sizer_3.SetEmptyCellSize(wx.Size(1, 18))
        buttons_sizer_4.Add(self.aux1_btn, wx.GBPosition(3, 0))
        buttons_sizer_4.Add(self.aux2_btn, wx.GBPosition(3, 1))
        buttons_sizer_4.Add(self.aux3_btn, wx.GBPosition(3, 2))
        buttons_sizer_4.Add(self.aux4_btn, wx.GBPosition(3, 3))
        buttons_sizer_4.Add(self.aux5_btn, wx.GBPosition(4, 0))
        buttons_sizer_4.Add(self.aux6_btn, wx.GBPosition(4, 1))
        buttons_sizer_4.Add(self.aux7_btn, wx.GBPosition(4, 2))
        buttons_sizer_4.Add(self.aux8_btn, wx.GBPosition(4, 3))

        buttons_sizer_5.Add(self.custom_btn, 0, flag=wx.ALL | wx.EXPAND)
        buttons_sizer_5.Add(self.always_on_top_switch, 0, wx.TOP, border=10)

        panel_sizer.Add(com_port_sizer, 0, wx.ALL, border=5)
        panel_sizer.Add(buttons_sizer_1, 0, wx.ALL, border=5)
        panel_sizer.AddSpacer(10)
        panel_sizer.Add(buttons_sizer_2, 0, wx.ALL, border=5)
        panel_sizer.AddSpacer(10)
        panel_sizer.Add(buttons_sizer_3, 0, wx.ALL, border=5)
        panel_sizer.AddSpacer(10)
        panel_sizer.Add(buttons_sizer_4, 0, wx.ALL, border=5)
        panel_sizer.AddSpacer(10)
        panel_sizer.Add(buttons_sizer_5, 0, wx.ALL, border=5)

        main_panel.SetSizer(panel_sizer)
        main_sizer.Add(main_panel, 1, wx.EXPAND)

        self.Bind(wx.EVT_CLOSE, self.on_exit)

    def send_command(self, *args):
        port = self.com_port.GetValue()
        try:
            ser = serial.Serial(port, 115200, timeout=1, write_timeout=1)
            for arg in args:
                ser.write(bytes(arg + "\n", "utf8"))
                time.sleep(0.05)
            ser.close()
        except serial.SerialException:
            pass

    def on_pwr_on_button(self, event):
        self.send_command("pwr on")

    def on_pwr_off_button(self, event):
        self.send_command("remote pwr")

    def on_input_button(self, event):
        self.send_command("remote input")

    def on_out_button(self, event):
        self.send_command("remote out")

    def on_scl_button(self, event):
        self.send_command("remote scl")

    def on_sfx_button(self, event):
        self.send_command("remote sfx")

    def on_adc_button(self, event):
        self.send_command("remote adc")

    def on_prof_button(self, event):
        self.send_command("remote prof")

    def on_num1_button(self, event):
        self.send_command("remote prof1")

    def on_num2_button(self, event):
        self.send_command("remote prof2")

    def on_num3_button(self, event):
        self.send_command("remote prof3")

    def on_num4_button(self, event):
        self.send_command("remote prof4")

    def on_num5_button(self, event):
        self.send_command("remote prof5")

    def on_num6_button(self, event):
        self.send_command("remote prof6")

    def on_num7_button(self, event):
        self.send_command("remote prof7")

    def on_num8_button(self, event):
        self.send_command("remote prof8")

    def on_num9_button(self, event):
        self.send_command("remote prof9")

    def on_num10_button(self, event):
        self.send_command("remote prof10")

    def on_num11_button(self, event):
        self.send_command("remote prof11")

    def on_num12_button(self, event):
        self.send_command("remote prof12")

    def on_menu_button(self, event):
        self.send_command("remote menu")

    def on_back_button(self, event):
        self.send_command("remote back")

    def on_ok_button(self, event):
        self.send_command("remote ok")

    def on_left_button(self, event):
        self.send_command("remote left")

    def on_right_button(self, event):
        self.send_command("remote right")

    def on_up_button(self, event):
        self.send_command("remote up")

    def on_down_button(self, event):
        self.send_command("remote down")

    def on_diag_button(self, event):
        self.send_command("remote diag")

    def on_stat_button(self, event):
        self.send_command("remote stat")

    def on_gain_button(self, event):
        self.send_command("remote gain")

    def on_pause_button(self, event):
        self.send_command("remote pause")

    def on_gen_button(self, event):
        self.send_command("remote genlock")

    def on_phase_button(self, event):
        self.send_command("remote phase")

    def on_safe_button(self, event):
        self.send_command("remote safe")

    def on_buffer_button(self, event):
        self.send_command("remote buffer")

    def on_res4k_button(self, event):
        self.send_command("remote res4k")

    def on_res1080p_button(self, event):
        self.send_command("remote res1080p")

    def on_res1440p_button(self, event):
        self.send_command("remote res1440p")

    def on_res480p_button(self, event):
        self.send_command("remote res480p")

    def on_res1_button(self, event):
        self.send_command("remote res1")

    def on_res2_button(self, event):
        self.send_command("remote res2")

    def on_res3_button(self, event):
        self.send_command("remote res3")

    def on_res4_button(self, event):
        self.send_command("remote res4")

    def on_aux1_button(self, event):
        self.send_command("remote aux1")

    def on_aux2_button(self, event):
        self.send_command("remote aux2")

    def on_aux3_button(self, event):
        self.send_command("remote aux3")

    def on_aux4_button(self, event):
        self.send_command("remote aux4")

    def on_aux5_button(self, event):
        self.send_command("remote aux5")

    def on_aux6_button(self, event):
        self.send_command("remote aux6")

    def on_aux7_button(self, event):
        self.send_command("remote aux7")

    def on_aux8_button(self, event):
        self.send_command("remote aux8")

    def on_custom_button(self, event):
        with wx.TextEntryDialog(self, "Custom Command:") as dialog:
            if dialog.ShowModal() == wx.ID_OK:
                custom = dialog.GetValue()
                if custom != "":
                    self.send_command(custom)

    def on_always_on_top(self, event):
        if self.always_on_top_switch.GetValue() is True:
            self.SetWindowStyle(
                wx.DEFAULT_FRAME_STYLE
                | wx.STAY_ON_TOP & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)
            )
        else:
            self.SetWindowStyle(
                wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)
            )
        event.Skip()

    def on_exit(self, event):
        self.config["port"] = self.com_port.GetValue()
        self.config["always_on_top"] = self.always_on_top_switch.GetValue()
        with open("config.json", "w") as config:
            config.write(json.dumps(self.config, indent=4))
        event.Skip()


if __name__ == "__main__":
    app = wx.App()
    frame = Frame(None, title="RT4K Remote")
    frame.Show()
    app.MainLoop()
