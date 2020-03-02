import pickle

pickle_file = open('data.txt', 'rb')
data = pickle.load(pickle_file)

title = []
for item in data:
  title.append(item['title'])
  #print(item['title'], 'item')
  #print(item['image_list'], 'item')

print('文章标题条数: %d' % (len(title)))

for t in title:
  print(t, 't')
