from  logging_logger import loggerClass

loggerClass.WritetoScreen(loggerClass,logging.INFO,"testing...",
            '%(levelname)s:%(message)s')

loggerClass.Writetofile(loggerClass,'sample.log',logging.WARNING,"testing...",
            '%(levelname)s:%(message)s')
