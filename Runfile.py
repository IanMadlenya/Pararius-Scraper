from Functions_HomePageStart import init_browser, navigate_to_website, enter_search_term, get_data

# Initialize browser & navigate to website

file_path = "local path to your driver"
browser = init_browser(file_path)
navigate_to_website(browser)

# Define search-term

search_term = "rotterdam"

# Enter search-term and get data

enter_search_term(browser, search_term)
get_data(browser, 4, search_term)


''''''
