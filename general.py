import os

# each website craweled will be in separate folder
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating Directory: ' + directory)
        os.makedirs(directory)
#create_project_dir('WebCrawler')

# create queue and crawled files (if not exists)
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue,base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

# create a new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()
#create_data_files('WebCrawler','https://facebook.com/')

# Append data to an existing files
def append_to_file(path,data):
    with open(path, 'a') as file: # open file in append mode
        file.write(data + '\n')

# delete the contents of a file
def delete_file_content(path):
    with open(path, 'w'):
        pass # keyword to do nothing

# Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    # empty set
    with open(file_name,'rt') as f:
        # open in read mode
        for line in f:
            results.add(line.replace('\n',''))
    return results


# iterate through a set , each item will be new line in the file
def set_to_file(links,file):
    delete_file_content(file)
    for link in sorted(links):
        append_to_file(file,link)    
