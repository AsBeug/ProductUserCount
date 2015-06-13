


def main():
    with open('Data/user_products.csv') as f:
        lines = f.readlines()
        for line in lines:
            parts = line.strip().split(',')
            u_id = parts[0]
            p_id = parts[1]

            print 'user: {0}; product: {1}'.format(u_id, p_id)

if __name__ == "__main__":
    main()