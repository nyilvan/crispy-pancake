import csv


def read_data(file_path):
    data = []


    with open(file_path, 'r', encoding='utf-8') as file:
        spreadsheet = csv.DictReader(file)

        for row in spreadsheet:
            data.append(row)

    return data


def get_rank(game):
    return int(game['rank'])


def search_games(data, query):
    results = []
    query = query.lower()


    for row in data:
        if query in row['name'].lower():
            results.append(row)


        results.sort(key=get_rank, reverse=True)


    return results


def run_search_tool():
    print("Welcome to Kata's Boardgame Search Tool!")
    print()
    print("You can search for board games by entering keywords.")
    print("Type the name of the game you want to find and press Enter.")
    print()
    print("*****")
    print()


    data = read_data('boardgames_ranks.csv')


    query = input("Enter your keywords here: ")


    results = search_games(data, query)


    if results:
        print(f"Found {len(results)} result(s):\n")

        for row in results:
            print(f"Name: {row['name']}, Year: {row['yearpublished']}, Rank: {row['rank']}")

    else:
        print("No matching results found.")



run_search_tool()