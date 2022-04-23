import json
from worker import Worker
from function import Function
from package import Package
from paSch import PaSch


def main():

    func_file = open('registry/functions1.json') #fetches functions from global registry
    fn = json.load(func_file)

    pkgs_file = open('registry/packages1.json')
    pkgs = json.load(pkgs_file)

    #list of globally declared functions fecthed from registry
    global_fn = []
    for x in fn:
        global_fn.append(
            Function(x["function_id"], x["function_imports"], x["function_size"]))

    # list of globally declared packages fecthed from registry
    global_pkgs = []
    for x in pkgs:
        global_pkgs.append(
            Package(x["package_id"], x["package_size"])
        )


       
    print("1.Demo run")
    print("2.Test cases")
    op = int(input("Choose an option: "))
    if(op==1):
        workers = [{"worker_id": "1", "threshold": 100},
                {"worker_id": "2", "threshold": 50},
                {"worker_id": "3", "threshold": 150}]

        test_workers = []
        test_hashworkers = []
        for x in workers:
            test_workers.append(Worker(x["worker_id"], x["threshold"]))
            test_hashworkers.append(x["worker_id"])

        scheduler = PaSch(test_hashworkers, test_workers,
                global_fn, global_pkgs)

        while True:
            print("\n")
            print("1. Add a new worker.")
            #print("2. Update an existing worker's threshold.")
            print("3. Remove a worker.")
            #print("4. View all workers.")
            print("5. View all functions in the registry.")
            print("6. View all packages in the registry.")
            print("7. Execute a function")
            print("8. Current state of system")
            print("9. Cache hits and miss")
            print("0. Exit")
            print("\n")
            option = int(input("Choose an option: "))
            print("\n")
            match option:
                case 1:
                    w_id = input("Enter worker id: ")
                    thres = int(input("Enter worker's threshold: "))
                    scheduler.addWorker(Worker(w_id,thres))

                    print("Worker {} successfully added!".format(w_id))
                case 3:
                    w_id = input("Enter worker id: ")
                    # for i, worker in enumerate(workers):
                    #     if w_id == worker["worker_id"]:
                    #         del workers[i]
                    # print("Worker {} successfully removed!".format(w_id))
                    scheduler.removeWorker(w_id)
                case 5:
                    print("Functions: ", fn)
                case 6:
                    print("Packages: ", pkgs)
                case 7:
                    f_id = input("Enter the function id: ")
                    t_stamp = int(input("Enter the timestamp: "))
                    print(scheduler.assignWorker(f_id, t_stamp))
                    
                    print("Function {} successfully executed!".format(f_id))
                case 8:
                    t_stamp = int(input("Enter the timestamp: "))
                    print(scheduler.getWorkerDetails(t_stamp))
                case 9:
                    details = scheduler.getCacheHitAndMissDetails()
                    print(details)
                case 0:
                    exit()
                case default:
                    continue
    else:
        print("2.Choose Test case number")
        op = int(input("Choose an option: "))
        print(op," :test case will be run")
        pkgs_file = open('test/'+str(op)+'.json')
        pkgs = json.load(pkgs_file)

        test_workers = []
        test_hashworkers = []
        workers = pkgs["workers"]  #workers are taken from the test/{i} file
        for x in workers:
            test_workers.append(Worker(x["worker_id"], x["threshold"]))
            test_hashworkers.append(x["worker_id"])

        scheduler = PaSch(test_hashworkers, test_workers,
                global_fn, global_pkgs)

        fn_execution = pkgs["functions"]
        for i in range (0,len(fn_execution)) :
            print(fn_execution[i])     
            print(scheduler.assignWorker(fn_execution[i]["fid"],fn_execution[i]["timestamp"]))   
        
        print(scheduler.getCacheHitAndMissDetails())
        # print(scheduler.getWorkerDetails(fn_execution[-1]["timestamp"]))
        
    

if __name__ == "__main__":
    main()
