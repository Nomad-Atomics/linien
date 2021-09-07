csr_constants = {
    "fast_a_iir_c_1_shift": 23,
    "fast_a_iir_c_1_width": 25,
    "fast_a_iir_c_1_interval": 1,
    "fast_a_iir_c_1_latency": 2,
    "fast_a_iir_c_1_order": 1,
    "fast_a_iir_c_1_iterative": 0,
    "fast_a_iir_d_1_shift": 23,
    "fast_a_iir_d_1_width": 25,
    "fast_a_iir_d_1_interval": 1,
    "fast_a_iir_d_1_latency": 3,
    "fast_a_iir_d_1_order": 2,
    "fast_a_iir_d_1_iterative": 0,
    "fast_a_iir_c_2_shift": 23,
    "fast_a_iir_c_2_width": 25,
    "fast_a_iir_c_2_interval": 1,
    "fast_a_iir_c_2_latency": 2,
    "fast_a_iir_c_2_order": 1,
    "fast_a_iir_c_2_iterative": 0,
    "fast_a_iir_d_2_shift": 23,
    "fast_a_iir_d_2_width": 25,
    "fast_a_iir_d_2_interval": 1,
    "fast_a_iir_d_2_latency": 3,
    "fast_a_iir_d_2_order": 2,
    "fast_a_iir_d_2_iterative": 0,
    "fast_b_iir_c_1_shift": 23,
    "fast_b_iir_c_1_width": 25,
    "fast_b_iir_c_1_interval": 1,
    "fast_b_iir_c_1_latency": 2,
    "fast_b_iir_c_1_order": 1,
    "fast_b_iir_c_1_iterative": 0,
    "fast_b_iir_d_1_shift": 23,
    "fast_b_iir_d_1_width": 25,
    "fast_b_iir_d_1_interval": 1,
    "fast_b_iir_d_1_latency": 3,
    "fast_b_iir_d_1_order": 2,
    "fast_b_iir_d_1_iterative": 0,
    "fast_b_iir_c_2_shift": 23,
    "fast_b_iir_c_2_width": 25,
    "fast_b_iir_c_2_interval": 1,
    "fast_b_iir_c_2_latency": 2,
    "fast_b_iir_c_2_order": 1,
    "fast_b_iir_c_2_iterative": 0,
    "fast_b_iir_d_2_shift": 23,
    "fast_b_iir_d_2_width": 25,
    "fast_b_iir_d_2_interval": 1,
    "fast_b_iir_d_2_latency": 3,
    "fast_b_iir_d_2_order": 2,
    "fast_b_iir_d_2_iterative": 0,
    "logic_sweep_shift": 24,
}

csr = {
    "dna_dna": (28, 0x000, 64, False),
    "fast_a_y_tap": (0, 0x000, 2, True),
    "fast_a_invert": (0, 0x001, 1, True),
    "fast_a_demod_delay": (0, 0x002, 32, True),
    "fast_a_demod_multiplier": (0, 0x006, 4, True),
    "fast_a_x_limit_1_min": (0, 0x007, 25, True),
    "fast_a_x_limit_1_max": (0, 0x00B, 25, True),
    "fast_a_iir_c_1_z0": (0, 0x00F, 27, True),
    "fast_a_iir_c_1_a1": (0, 0x013, 25, True),
    "fast_a_iir_c_1_b0": (0, 0x017, 25, True),
    "fast_a_iir_c_1_b1": (0, 0x01B, 25, True),
    "fast_a_iir_d_1_z0": (0, 0x01F, 27, True),
    "fast_a_iir_d_1_a1": (0, 0x023, 25, True),
    "fast_a_iir_d_1_a2": (0, 0x027, 25, True),
    "fast_a_iir_d_1_b0": (0, 0x02B, 25, True),
    "fast_a_iir_d_1_b1": (0, 0x02F, 25, True),
    "fast_a_iir_d_1_b2": (0, 0x033, 25, True),
    "fast_a_y_limit_1_min": (0, 0x037, 25, True),
    "fast_a_y_limit_1_max": (0, 0x03B, 25, True),
    "fast_a_x_limit_2_min": (0, 0x03F, 25, True),
    "fast_a_x_limit_2_max": (0, 0x043, 25, True),
    "fast_a_iir_c_2_z0": (0, 0x047, 27, True),
    "fast_a_iir_c_2_a1": (0, 0x04B, 25, True),
    "fast_a_iir_c_2_b0": (0, 0x04F, 25, True),
    "fast_a_iir_c_2_b1": (0, 0x053, 25, True),
    "fast_a_iir_d_2_z0": (0, 0x057, 27, True),
    "fast_a_iir_d_2_a1": (0, 0x05B, 25, True),
    "fast_a_iir_d_2_a2": (0, 0x05F, 25, True),
    "fast_a_iir_d_2_b0": (0, 0x063, 25, True),
    "fast_a_iir_d_2_b1": (0, 0x067, 25, True),
    "fast_a_iir_d_2_b2": (0, 0x06B, 25, True),
    "fast_a_y_limit_2_min": (0, 0x06F, 25, True),
    "fast_a_y_limit_2_max": (0, 0x073, 25, True),
    "fast_a_x_clr": (0, 0x077, 1, True),
    "fast_a_x_max": (0, 0x078, 25, False),
    "fast_a_x_min": (0, 0x07C, 25, False),
    "fast_a_out_i_clr": (0, 0x080, 1, True),
    "fast_a_out_i_max": (0, 0x081, 25, False),
    "fast_a_out_i_min": (0, 0x085, 25, False),
    "fast_a_out_q_clr": (0, 0x089, 1, True),
    "fast_a_out_q_max": (0, 0x08A, 25, False),
    "fast_a_out_q_min": (0, 0x08E, 25, False),
    "fast_a_dx_sel": (0, 0x092, 4, True),
    "fast_a_dy_sel": (0, 0x093, 4, True),
    "fast_b_y_tap": (1, 0x000, 2, True),
    "fast_b_invert": (1, 0x001, 1, True),
    "fast_b_demod_delay": (1, 0x002, 32, True),
    "fast_b_demod_multiplier": (1, 0x006, 4, True),
    "fast_b_x_limit_1_min": (1, 0x007, 25, True),
    "fast_b_x_limit_1_max": (1, 0x00B, 25, True),
    "fast_b_iir_c_1_z0": (1, 0x00F, 27, True),
    "fast_b_iir_c_1_a1": (1, 0x013, 25, True),
    "fast_b_iir_c_1_b0": (1, 0x017, 25, True),
    "fast_b_iir_c_1_b1": (1, 0x01B, 25, True),
    "fast_b_iir_d_1_z0": (1, 0x01F, 27, True),
    "fast_b_iir_d_1_a1": (1, 0x023, 25, True),
    "fast_b_iir_d_1_a2": (1, 0x027, 25, True),
    "fast_b_iir_d_1_b0": (1, 0x02B, 25, True),
    "fast_b_iir_d_1_b1": (1, 0x02F, 25, True),
    "fast_b_iir_d_1_b2": (1, 0x033, 25, True),
    "fast_b_y_limit_1_min": (1, 0x037, 25, True),
    "fast_b_y_limit_1_max": (1, 0x03B, 25, True),
    "fast_b_x_limit_2_min": (1, 0x03F, 25, True),
    "fast_b_x_limit_2_max": (1, 0x043, 25, True),
    "fast_b_iir_c_2_z0": (1, 0x047, 27, True),
    "fast_b_iir_c_2_a1": (1, 0x04B, 25, True),
    "fast_b_iir_c_2_b0": (1, 0x04F, 25, True),
    "fast_b_iir_c_2_b1": (1, 0x053, 25, True),
    "fast_b_iir_d_2_z0": (1, 0x057, 27, True),
    "fast_b_iir_d_2_a1": (1, 0x05B, 25, True),
    "fast_b_iir_d_2_a2": (1, 0x05F, 25, True),
    "fast_b_iir_d_2_b0": (1, 0x063, 25, True),
    "fast_b_iir_d_2_b1": (1, 0x067, 25, True),
    "fast_b_iir_d_2_b2": (1, 0x06B, 25, True),
    "fast_b_y_limit_2_min": (1, 0x06F, 25, True),
    "fast_b_y_limit_2_max": (1, 0x073, 25, True),
    "fast_b_x_clr": (1, 0x077, 1, True),
    "fast_b_x_max": (1, 0x078, 25, False),
    "fast_b_x_min": (1, 0x07C, 25, False),
    "fast_b_out_i_clr": (1, 0x080, 1, True),
    "fast_b_out_i_max": (1, 0x081, 25, False),
    "fast_b_out_i_min": (1, 0x085, 25, False),
    "fast_b_out_q_clr": (1, 0x089, 1, True),
    "fast_b_out_q_max": (1, 0x08A, 25, False),
    "fast_b_out_q_min": (1, 0x08E, 25, False),
    "fast_b_dx_sel": (1, 0x092, 4, True),
    "fast_b_dy_sel": (1, 0x093, 4, True),
    "gpio_n_ins": (30, 0x000, 8, False),
    "gpio_n_outs": (30, 0x001, 8, True),
    "gpio_n_oes": (30, 0x002, 8, True),
    "gpio_n_state": (30, 0x003, 14, False),
    "gpio_n_state_clr": (30, 0x005, 1, True),
    "gpio_n_do0_en": (30, 0x006, 14, True),
    "gpio_n_do1_en": (30, 0x008, 14, True),
    "gpio_n_do2_en": (30, 0x00A, 14, True),
    "gpio_n_do3_en": (30, 0x00C, 14, True),
    "gpio_n_do4_en": (30, 0x00E, 14, True),
    "gpio_n_do5_en": (30, 0x010, 14, True),
    "gpio_n_do6_en": (30, 0x012, 14, True),
    "gpio_n_do7_en": (30, 0x014, 14, True),
    "gpio_p_ins": (31, 0x000, 8, False),
    "gpio_p_outs": (31, 0x001, 8, True),
    "gpio_p_oes": (31, 0x002, 8, True),
    "logic_dual_channel": (8, 0x000, 1, True),
    "logic_chain_a_factor": (8, 0x001, 9, True),
    "logic_chain_b_factor": (8, 0x003, 9, True),
    "logic_chain_a_offset": (8, 0x005, 14, True),
    "logic_chain_b_offset": (8, 0x007, 14, True),
    "logic_combined_offset": (8, 0x009, 14, True),
    "logic_out_offset": (8, 0x00B, 14, True),
    "logic_mod_channel": (8, 0x00D, 1, True),
    "logic_control_channel": (8, 0x00E, 1, True),
    "logic_sweep_channel": (8, 0x00F, 2, True),
    "logic_slow_value": (8, 0x010, 14, False),
    "logic_slow_decimation": (8, 0x012, 5, True),
    "logic_analog_out_1": (8, 0x013, 15, True),
    "logic_analog_out_2": (8, 0x015, 15, True),
    "logic_analog_out_3": (8, 0x017, 15, True),
    "logic_mod_amp": (8, 0x019, 14, True),
    "logic_mod_freq": (8, 0x01B, 32, True),
    "logic_sweep_step": (8, 0x01F, 30, True),
    "logic_sweep_min": (8, 0x023, 14, True),
    "logic_sweep_max": (8, 0x025, 14, True),
    "logic_sweep_run": (8, 0x027, 1, True),
    "logic_limit_error_signal_min": (8, 0x028, 25, True),
    "logic_limit_error_signal_max": (8, 0x02C, 25, True),
    "logic_limit_fast1_min": (8, 0x030, 14, True),
    "logic_limit_fast1_max": (8, 0x032, 14, True),
    "logic_limit_fast2_min": (8, 0x034, 14, True),
    "logic_limit_fast2_max": (8, 0x036, 14, True),
    "logic_pid_setpoint": (8, 0x038, 25, True),
    "logic_pid_kp": (8, 0x03C, 14, True),
    "logic_pid_ki": (8, 0x03E, 14, True),
    "logic_pid_reset": (8, 0x040, 1, True),
    "logic_pid_kd": (8, 0x041, 14, True),
    "logic_autolock_robust_time_scale": (8, 0x043, 14, True),
    "logic_autolock_robust_N_instructions": (8, 0x045, 5, True),
    "logic_autolock_robust_final_wait_time": (8, 0x046, 14, True),
    "logic_autolock_robust_peak_height_0": (8, 0x048, 28, True),
    "logic_autolock_robust_peak_height_1": (8, 0x04C, 28, True),
    "logic_autolock_robust_peak_height_2": (8, 0x050, 28, True),
    "logic_autolock_robust_peak_height_3": (8, 0x054, 28, True),
    "logic_autolock_robust_peak_height_4": (8, 0x058, 28, True),
    "logic_autolock_robust_peak_height_5": (8, 0x05C, 28, True),
    "logic_autolock_robust_peak_height_6": (8, 0x060, 28, True),
    "logic_autolock_robust_peak_height_7": (8, 0x064, 28, True),
    "logic_autolock_robust_peak_height_8": (8, 0x068, 28, True),
    "logic_autolock_robust_peak_height_9": (8, 0x06C, 28, True),
    "logic_autolock_robust_peak_height_10": (8, 0x070, 28, True),
    "logic_autolock_robust_peak_height_11": (8, 0x074, 28, True),
    "logic_autolock_robust_peak_height_12": (8, 0x078, 28, True),
    "logic_autolock_robust_peak_height_13": (8, 0x07C, 28, True),
    "logic_autolock_robust_peak_height_14": (8, 0x080, 28, True),
    "logic_autolock_robust_peak_height_15": (8, 0x084, 28, True),
    "logic_autolock_robust_peak_height_16": (8, 0x088, 28, True),
    "logic_autolock_robust_peak_height_17": (8, 0x08C, 28, True),
    "logic_autolock_robust_peak_height_18": (8, 0x090, 28, True),
    "logic_autolock_robust_peak_height_19": (8, 0x094, 28, True),
    "logic_autolock_robust_peak_height_20": (8, 0x098, 28, True),
    "logic_autolock_robust_peak_height_21": (8, 0x09C, 28, True),
    "logic_autolock_robust_peak_height_22": (8, 0x0A0, 28, True),
    "logic_autolock_robust_peak_height_23": (8, 0x0A4, 28, True),
    "logic_autolock_robust_peak_height_24": (8, 0x0A8, 28, True),
    "logic_autolock_robust_peak_height_25": (8, 0x0AC, 28, True),
    "logic_autolock_robust_peak_height_26": (8, 0x0B0, 28, True),
    "logic_autolock_robust_peak_height_27": (8, 0x0B4, 28, True),
    "logic_autolock_robust_peak_height_28": (8, 0x0B8, 28, True),
    "logic_autolock_robust_peak_height_29": (8, 0x0BC, 28, True),
    "logic_autolock_robust_peak_height_30": (8, 0x0C0, 28, True),
    "logic_autolock_robust_peak_height_31": (8, 0x0C4, 28, True),
    "logic_autolock_robust_wait_for_0": (8, 0x0C8, 14, True),
    "logic_autolock_robust_wait_for_1": (8, 0x0CA, 14, True),
    "logic_autolock_robust_wait_for_2": (8, 0x0CC, 14, True),
    "logic_autolock_robust_wait_for_3": (8, 0x0CE, 14, True),
    "logic_autolock_robust_wait_for_4": (8, 0x0D0, 14, True),
    "logic_autolock_robust_wait_for_5": (8, 0x0D2, 14, True),
    "logic_autolock_robust_wait_for_6": (8, 0x0D4, 14, True),
    "logic_autolock_robust_wait_for_7": (8, 0x0D6, 14, True),
    "logic_autolock_robust_wait_for_8": (8, 0x0D8, 14, True),
    "logic_autolock_robust_wait_for_9": (8, 0x0DA, 14, True),
    "logic_autolock_robust_wait_for_10": (8, 0x0DC, 14, True),
    "logic_autolock_robust_wait_for_11": (8, 0x0DE, 14, True),
    "logic_autolock_robust_wait_for_12": (8, 0x0E0, 14, True),
    "logic_autolock_robust_wait_for_13": (8, 0x0E2, 14, True),
    "logic_autolock_robust_wait_for_14": (8, 0x0E4, 14, True),
    "logic_autolock_robust_wait_for_15": (8, 0x0E6, 14, True),
    "logic_autolock_robust_wait_for_16": (8, 0x0E8, 14, True),
    "logic_autolock_robust_wait_for_17": (8, 0x0EA, 14, True),
    "logic_autolock_robust_wait_for_18": (8, 0x0EC, 14, True),
    "logic_autolock_robust_wait_for_19": (8, 0x0EE, 14, True),
    "logic_autolock_robust_wait_for_20": (8, 0x0F0, 14, True),
    "logic_autolock_robust_wait_for_21": (8, 0x0F2, 14, True),
    "logic_autolock_robust_wait_for_22": (8, 0x0F4, 14, True),
    "logic_autolock_robust_wait_for_23": (8, 0x0F6, 14, True),
    "logic_autolock_robust_wait_for_24": (8, 0x0F8, 14, True),
    "logic_autolock_robust_wait_for_25": (8, 0x0FA, 14, True),
    "logic_autolock_robust_wait_for_26": (8, 0x0FC, 14, True),
    "logic_autolock_robust_wait_for_27": (8, 0x0FE, 14, True),
    "logic_autolock_robust_wait_for_28": (8, 0x100, 14, True),
    "logic_autolock_robust_wait_for_29": (8, 0x102, 14, True),
    "logic_autolock_robust_wait_for_30": (8, 0x104, 14, True),
    "logic_autolock_robust_wait_for_31": (8, 0x106, 14, True),
    "logic_autolock_fast_target_position": (8, 0x108, 14, True),
    "logic_autolock_request_lock": (8, 0x10A, 1, True),
    "logic_autolock_autolock_mode": (8, 0x10B, 2, True),
    "logic_autolock_lock_running": (8, 0x10C, 1, False),
    "logic_control_signal_clr": (8, 0x10D, 1, True),
    "logic_control_signal_max": (8, 0x10E, 25, False),
    "logic_control_signal_min": (8, 0x112, 25, False),
    "logic_combined_error_signal_clr": (8, 0x116, 1, True),
    "logic_combined_error_signal_max": (8, 0x117, 25, False),
    "logic_combined_error_signal_min": (8, 0x11B, 25, False),
    "scopegen_external_trigger": (6, 0x000, 1, True),
    "scopegen_dac_a_clr": (6, 0x001, 1, True),
    "scopegen_dac_a_max": (6, 0x002, 25, False),
    "scopegen_dac_a_min": (6, 0x006, 25, False),
    "scopegen_dac_b_clr": (6, 0x00A, 1, True),
    "scopegen_dac_b_max": (6, 0x00B, 25, False),
    "scopegen_dac_b_min": (6, 0x00F, 25, False),
    "scopegen_adc_a_sel": (6, 0x013, 4, True),
    "scopegen_adc_b_sel": (6, 0x014, 4, True),
    "scopegen_adc_a_q_sel": (6, 0x015, 4, True),
    "scopegen_adc_b_q_sel": (6, 0x016, 4, True),
    "slow_pid_setpoint": (2, 0x000, 14, True),
    "slow_pid_kp": (2, 0x002, 14, True),
    "slow_pid_ki": (2, 0x004, 14, True),
    "slow_pid_reset": (2, 0x006, 1, True),
    "slow_pid_kd": (2, 0x007, 14, True),
    "slow_limit_min": (2, 0x009, 14, True),
    "slow_limit_max": (2, 0x00B, 14, True),
    "slow_out_clr": (2, 0x00D, 1, True),
    "slow_out_max": (2, 0x00E, 25, False),
    "slow_out_min": (2, 0x012, 25, False),
    "xadc_temp": (29, 0x000, 12, False),
    "xadc_v": (29, 0x002, 12, False),
    "xadc_a": (29, 0x004, 12, False),
    "xadc_b": (29, 0x006, 12, False),
    "xadc_c": (29, 0x008, 12, False),
    "xadc_d": (29, 0x00A, 12, False),
}
states = [
    "force",
    "di0",
    "di1",
    "di2",
    "di3",
    "di4",
    "di5",
    "di6",
    "di7",
    "robust_watching",
    "robust_turn_on_lock",
    "robust_sign_equal",
    "robust_over_threshold",
    "robust_waited_long_enough",
]
signals = [
    "zero",
    "fast_a_x",
    "fast_a_out_i",
    "fast_a_out_q",
    "fast_b_x",
    "fast_b_out_i",
    "fast_b_out_q",
    "slow_out",
    "scopegen_dac_a",
    "scopegen_dac_b",
    "logic_control_signal",
    "logic_combined_error_signal",
]
