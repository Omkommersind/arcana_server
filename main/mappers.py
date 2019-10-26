class RequestToCategoriesMapper:
    @staticmethod
    def map(data):
        categories = None
        if 'categories' in data:
            categories = data['categories'].split(',')

        return categories
