class demo(multiprocessing.Process):
    def __init__(self, args):
        multiprocessing.Process.__init__(self)

        self.index = args[0]
        self.dict = {}
        # 传入的参数存入临时字典
        self.dict['process_name'] = args[1]['process_name']
        ...          
        

    def run(self):
        sys.stdout = Logger(process_name=self.dict['process_name'])
        try:
            while True:
                # 在这里写天勤策略的代码
                pass

        except Exception as ex:
            print("exception catched: %r" % ex)
            sys.exit(1)
