def get_dataset_info(trace_name):
    if trace_name == 'alibaba2018':
        dataset_info = {
            "timestamp_frequency_secs": 300,
            "column_config": {
                "cpu_util_percent": {
                    "column_index": 0,
                    "y_axis_min": 0,
                    "y_axis_max": 100
                },
                "mem_util_percent": {
                    "column_index": 1,
                    "y_axis_min": 0,
                    "y_axis_max": 100
                },
                "net_in": {
                    "column_index": 2,
                    "y_axis_min": 0,
                    "y_axis_max": 100
                },
                "net_out": {
                    "column_index": 3,
                    "y_axis_min": 0,
                    "y_axis_max": 100
                },
                "disk_io_percent": {
                    "column_index": 4,
                    "y_axis_min": 0,
                    "y_axis_max": 100
                }

            },
            "metadata": {
                "fields": {
                    "cpu_util_percent": {
                        "type": "numerical",
                        "subtype": "float"
                    },
                    "mem_util_percent": {
                        "type": "numerical",
                        "subtype": "float"
                    },
                    "net_in": {
                        "type": "numerical",
                        "subtype": "float"
                    },
                    "net_out": {
                        "type": "numerical",
                        "subtype": "float"
                    },
                    "disk_io_percent": {
                        "type": "numerical",
                        "subtype": "float"
                    }
                }
            }
        }
    if trace_name == 'alibaba2018-4columns':
        dataset_info = {
            "timestamp_frequency_secs": 300,
            "column_config": {
                "mem_util_percent": {
                    "column_index": 0,
                    "y_axis_min": 0,
                    "y_axis_max": 100
                },
                "net_in": {
                    "column_index": 1,
                    "y_axis_min": 0,
                    "y_axis_max": 100
                },
                "net_out": {
                    "column_index": 2,
                    "y_axis_min": 0,
                    "y_axis_max": 100
                },
                "disk_io_percent": {
                    "column_index": 3,
                    "y_axis_min": 0,
                    "y_axis_max": 100
                }

            },
            "metadata": {
                "fields": {
                    "mem_util_percent": {
                        "type": "numerical",
                        "subtype": "float"
                    },
                    "net_in": {
                        "type": "numerical",
                        "subtype": "float"
                    },
                    "net_out": {
                        "type": "numerical",
                        "subtype": "float"
                    },
                    "disk_io_percent": {
                        "type": "numerical",
                        "subtype": "float"
                    }
                }
            }
        }
    elif trace_name == 'google2019':
        dataset_info = {
            "timestamp_frequency_secs": 300,
            "column_config": {
                "cpu": {
                    "column_index": 0,
                    "y_axis_min": 0,
                    "y_axis_max": 1
                },
                "mem": {
                    "column_index": 1,
                    "y_axis_min": 0,
                    "y_axis_max": 1
                },
                "assigned_mem": {
                    "column_index": 2,
                    "y_axis_min": 0,
                    "y_axis_max": 1
                },
                "cycles_per_instruction": {
                    "column_index": 3
                }
            },
            "metadata": {
                "fields": {
                    "cpu": {
                        "type": "numerical",
                        "subtype": "float"
                    },
                    "mem": {
                        "type": "numerical",
                        "subtype": "float"
                    },
                    "assigned_mem": {
                        "type": "numerical",
                        "subtype": "float"
                    },
                    "cycles_per_instruction": {
                        "type": "numerical",
                        "subtype": "float"
                    }
                }
            }
        }
    elif trace_name == 'azure_v2':
        dataset_info = {
            "timestamp_frequency_secs": 300,
            "column_config": {
                "cpu_total": {
                    "column_index": 0
                },
                "mem_total": {
                    "column_index": 1
                }
            },
            "metadata": {
                "fields": {
                    "cpu_total": {
                        "type": "numerical",
                        "subtype": "float"
                    },
                    "mem_total": {
                        "type": "numerical",
                        "subtype": "float"
                    }
                }
            }
        }
    elif trace_name == 'reddit':
        dataset_info = {
            "timestamp_frequency_secs": 3600,
            "column_config": {
                "interactions": {
                    "column_index": 0
                }
            }
        }
    return dataset_info
