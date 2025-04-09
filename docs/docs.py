get_reservations_responses = {
        200: {
            "description": "Успешное выполнение запроса.",
            "content": {
                "application/json": {
                    "example": {
                        "data": [
                            {
                                "id": 1,
                                "table_id": 1,
                                "customer_name": "Дмитрий",
                                "reservation_time": "2025-04-09 12:29:38",
                                "duration_minutes": 40
                            }
                        ]
                    }
                }
            }
        },
        500: {
            "description": "Ошибка на стороне сервиса.",
            "content": {
                "application/json": {
                    "example": {
                        "error": "Ошибка: Во время получения резерва столов произошла ошибка.",
                    }
                }
            }
        }
    }

post_reservations_responses = {
    200: {
        "description": "Успешное выполнение запроса.",
        "content": {
            "application/json": {
                "example":
                    {
                        "data": "Бронь успешно создана."
                    }
            }
        }
    },
    400: {
        "description": "Ошибка исполнения процесса.",
        "content": {
            "application/json": {
                "example": [
                    {
                        "error": "Ошибка: Не удалось создать бронь. Повторите попытку."
                    },
                    {
                        "error": "Ошибка: В указанное время стол уже зарезервирован."
                    },
                    {
                        "error": "Ошибка: Указанного стола не существует. Проверьте столы."
                    }
                ]
            }
        }
    },
    500: {
        "description": "Ошибка на стороне сервиса.",
        "content": {
            "application/json": {
                "example": {
                    "error": "Ошибка: Во время создания резерва стола произошла ошибка.",

                }
            }
        }
    }
}

delete_reservations_responses = {
    200: {
        "description": "Успешное выполнение запроса.",
        "content": {
            "application/json": {
                "example":
                    {
                        "data": "Бронь успешно удалена."
                    }
            }
        }
    },
    400: {
        "description": "Ошибка исполнения процесса.",
        "content": {
            "application/json": {
                "example":
                    {
                        "error": "Ошибка: Не удалось удалить бронь. Проверьте ее наличие."
                    }
            }
        }
    },
    500: {
        "description": "Ошибка на стороне сервиса.",
        "content": {
            "application/json": {
                "example": {
                    "error": "Ошибка: Во время удаления брони произошла ошибка.",
                }
            }
        }
    }
}

get_tables_responses = {
        200: {
            "description": "Успешное выполнение запроса.",
            "content": {
                "application/json": {
                    "example": {
                        "data": [
                            {
                                "id": 2,
                                "name": "Стол 7",
                                "seats": 5,
                                "location": "Центр зала"
                            }
                        ]
                    }
                }
            }
        },
        500: {
            "description": "Ошибка на стороне сервиса.",
            "content": {
                "application/json": {
                    "example": {
                        "error": "Ошибка: Во время получения столов произошла ошибка."
                    }
                }
            }
        }
    }

post_tables_responses = {
    200: {
        "description": "Успешное выполнение запроса.",
        "content": {
            "application/json": {
                "example":
                    {
                        "data": "Стол успешно создан."
                    }
            }
        }
    },
    400: {
        "description": "Ошибка исполнения процесса.",
        "content": {
            "application/json": {
                "example": [
                    {
                        "error": "Ошибка: Стол с таким именем уже существует."
                    },
                    {
                        "error": "Ошибка: Не удалось создать стол. Повторите попытку."
                    }
                ]
            }
        }
    },
    500: {
        "description": "Ошибка на стороне сервиса.",
        "content": {
            "application/json": {
                "example": {
                    "error": "Ошибка: Во время создания стола произошла ошибка."
                }
            }
        }
    }
}

delete_tables_responses = {
    200: {
        "description": "Успешное выполнение запроса.",
        "content": {
            "application/json": {
                "example":
                    {
                        "data": "Стол успешно удален."
                    }
            }
        }
    },
    400: {
        "description": "Ошибка исполнения процесса.",
        "content": {
            "application/json": {
                "example": [
                    {
                        "error": "Ошибка: Не удалось удалить стол. Стол не найден."
                    },
                    {
                        "error": "Ошибка: Невозможно удалить стол, возможно он зарезервирован. Проверьте брони стола."
                    }
                ]
            }
        }
    },
    500: {
        "description": "Ошибка на стороне сервиса.",
        "content": {
            "application/json": {
                "example": {
                    "error": "Ошибка: Во время удаления стола произошла ошибка."
                }
            }
        }
    }
}
