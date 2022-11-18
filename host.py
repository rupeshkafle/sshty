class Host:
    olt_list = {
        1:{'olt-1':'127.0.0.1'},
        2:{'olt-2':'127.0.0.2'},
        3:{'olt-3':'127.0.0.3'}
    }
    switch_list = {
        1:{'switch-1':'127.0.0.1'},
        2:{'switch-2':'127.0.0.2'},
        3:{'switch-3':'127.0.0.3'}
    }
    router_list = {
        1:{'router-1':'127.0.0.1'},
        2:{'router-2':'127.0.0.2'},
        3:{'router-3':'127.0.0.3'}
    }
    server_list = {
        1:{'server-1':'127.0.0.1'},
        2:{'server-2':'127.0.0.2'},
        3:{'server-3':'127.0.0.3'}
    }
    main_options = {
        1:{'OLT':olt_list},
        2:{'Switch':switch_list},
        3:{'Router':router_list},
        4:{'Server':server_list}
    }
    def getHost(self):
        # Display main menu options and select a category
        for key, value in self.main_options.items():
            print(f"{key}. {list(value.keys())[0]}")
        selected_category = int(input("Please choose a category: "))
        category = list(self.main_options.get(selected_category).values())[0]

        # Display menu options of selected category and select a host
        for key, value in category.items():
            print(f"{key}. {list(value.keys())[0]}")
        selected_option = int(input("Select a server: "))
        
        return list(category.get(selected_option).values())[0]
