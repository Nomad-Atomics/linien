import numpy as np
from PyQt5 import QtGui

from linien.common import convert_channel_mixing_value
from linien.client.widgets import CustomWidget
from linien.client.connection import MHz, Vpp


class GeneralPanel(QtGui.QWidget, CustomWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def ready(self):
        self.ids.rampOnSlow.stateChanged.connect(self.ramp_on_slow_changed)
        self.ids.channel_mixing_slider.valueChanged.connect(self.channel_mixing_changed)
        self.ids.dual_channel.stateChanged.connect(self.dual_channel_changed)

    def connection_established(self):
        params = self.app().parameters
        self.control = self.app().control
        self.parameters = params

        def ramp_on_slow_param_changed(value):
            self.ids.rampOnSlow.setChecked(value)
            self.ids.explainSweepOnAnalog.setVisible(value)
            self.ids.explainNoSweepOnAnalog.setVisible(not value)

        params.ramp_on_slow.change(ramp_on_slow_param_changed)

        def dual_channel_changed(value):
            self.ids.dual_channel.setChecked(value)
            self.ids.dual_channel_mixing.setVisible(value)
            self.ids.explain_second_channel.setVisible(value)
            self.app().main_window.ids.spectroscopy_channel_2_page.setEnabled(value)

        params.dual_channel.change(dual_channel_changed)

        def channel_mixing_changed(value):
            # FIXME: blockSignals überall?
            self.ids.channel_mixing_slider.blockSignals(True)
            self.ids.channel_mixing_slider.setValue(value + 128)
            self.ids.channel_mixing_slider.blockSignals(False)

            self.update_channel_mixing_slider(value)
        params.channel_mixing.change(channel_mixing_changed)

    def ramp_on_slow_changed(self):
        self.parameters.ramp_on_slow.value = int(self.ids.rampOnSlow.checkState() > 0)
        self.control.write_data()

    def channel_mixing_changed(self):
        value = int(self.ids.channel_mixing_slider.value()) - 128
        self.parameters.channel_mixing.value = value
        self.control.write_data()

        self.update_channel_mixing_slider(value)

    def dual_channel_changed(self):
        self.parameters.dual_channel.value = int(self.ids.dual_channel.checkState() > 0)
        self.control.write_data()

    def update_channel_mixing_slider(self, value):
        a_value, b_value = convert_channel_mixing_value(value)

        self.ids.chain_a_factor.setText('%d' % a_value)
        self.ids.chain_b_factor.setText('%d' % b_value)