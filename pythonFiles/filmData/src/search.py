from util import secure_input

def basic_search(array_params, array_bools, session):
    is_film, is_age, is_id, is_location = array_bools
    if is_film:
        session.get_cursor().callproc('basicNameSearch', array_params[0])
        session.print_results()
    elif is_age:
        session.get_cursor().callproc('basicAgeSearch', array_params[1])
        session.print_results()
    elif is_id:
        session.get_cursor().callproc('basicIdSearch', array_params[2])
        session.print_results()
    elif is_location:
        session.get_cursor().callproc('basicLocationSearch', array_params[3])
        session.print_results()
    else :
        print("An Unrecoverable Error Occurred!")

def double_search(array_params, array_bools, session):
    is_film, is_age, is_id, is_location = array_bools
    if is_id and is_location:
        session.get_cursor().callproc('idLocationSearch', array_params[2] + array_params[3])
        session.print_results()
    elif is_id and is_age:
        session.get_cursor().callproc('idAgeSearch', array_params[2] + array_params[1])
        session.print_results()
    elif is_id and is_film:
        session.get_cursor().callproc('idNameSearch', array_params[2] + array_params[0])
        session.print_results()
    elif is_film and is_location:
        session.get_cursor().callproc('nameLocationSearch', array_params[0] + array_params[3])
        session.print_results()
    elif is_film and is_age:
        session.get_cursor().callproc('nameAgeSearch', array_params[0] + array_params[1])
        session.print_results()
    elif is_location and is_age:
        session.get_cursor().callproc('locationAgeSearch', array_params[3] + array_params[1])
        session.print_results()
    else :
        print("An Unrecoverable Error Occurred!")

def triple_search(array_params, array_bools, session):
    is_film, is_age, is_id, is_location = array_bools
    if is_id and is_location and is_age:
        session.get_cursor().callproc('idLocationAgeSearch', array_params[2] + array_params[3] + array_params[1])
        session.print_results()
    elif is_id and is_film and is_age:
        session.get_cursor().callproc('idNameAgeSearch', array_params[2] + array_params[0] + array_params[1])
        session.print_results()
    elif is_id and is_film and is_location:
        session.get_cursor().callproc('idNameLocationSearch', array_params[2] + array_params[0] + array_params[3])
        session.print_results()
    elif is_film and is_location and is_age:
        session.get_cursor().callproc('nameLocationAgeSearch', array_params[0] + array_params[3] + array_params[1])
        session.print_results()
    else :
        print("An Unrecoverable Error Occurred!")

def grand_slam_search(array_params, array_bools, session):
    is_film, is_age, is_id, is_location = array_bools
    if is_id and is_film and is_location and is_age:
        session.get_cursor().callproc('idNameLocationAgeSearch', array_params[2] + array_params[0] + array_params[3] + array_params[1])
        session.print_results()

def get_bools(array_params):
    bool_list = []
    counter = 0
    for param in array_params:
        if not param :
            bool_list.append(True == False)
        else :
            bool_list.append(True == True)
            counter += 1
    return counter, bool_list


def launch_search(array_params, array_bools, counter, session):
    match counter:
        case 0 :
            # Get All Films
            session.get_cursor().callproc('getAll')
            session.print_results()
        case 1 :
            # Search with one parameter
            basic_search(array_params, array_bools, session)
        case 2 :
            # Search with two parameters
            double_search(array_params, array_bools, session)
        case 3 :
            # Search with three parameters
            triple_search(array_params, array_bools, session)
        case 4 :
            # Search with four parameters
            grand_slam_search(array_params, array_bools, session)
        case _ :
            # Invalid
            exit("An unrecoverable error occurred!")



def search_fun(session):
    print("Welcome to Search!")
    print("Separate multiple entries with spaces")
    film_name = input("Enter film name (to search by name or press enter to leave blank)\n")
    age_rating = input("Enter any amount of age ratings (to search by age or press enter to leave blank)\n").split()
    id_number = input("Enter an id (to search by id or press enter to leave blank)\n")
    location = input("Enter any amount of locations (to search by location or press enter to leave blank)\n").split()

    if age_rating :
        while len(age_rating) < 7:
            age_rating.append("")
    if location :
        while len(location) < 3:
            location.append("")
    if film_name:
        film_name = [film_name]
    if id_number:
        id_number = [id_number]

    print(f"You entered:\n{film_name}\n{age_rating}\n{id_number}\n{location}")
    while True :
        command = secure_input("If you are happy with these type GO, type REENTER to re-enter and type MAIN to return to main menu\n").strip().split()[0].upper()
        match command:
            case "GO":
                array_params = (film_name, age_rating, id_number, location)
                counter, array_bools = get_bools(array_params)
                launch_search(array_params, array_bools, counter, session)
                break
            case "REENTER":
                search_fun(session)
                break
            case "MAIN":
                return
            case _:
                print("Command not recognised!")