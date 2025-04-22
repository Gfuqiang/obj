import datetime
import time


class Bucket:

    def __init__(self, capacity, rate):
        self.bucket_capacity = capacity
        self.rate = rate
        self.last_add_time = datetime.datetime.now()
        self.token_num = capacity

    def refill(self):
        add_token_num = int((datetime.datetime.now() - self.last_add_time).seconds) * self.rate
        self.token_num = min(self.bucket_capacity, self.token_num + add_token_num)
        self.last_add_time = datetime.datetime.now()

    def consumer(self):
        if self.token_num <= 0:
            return False
        self.token_num -= 1
        return True


def simulate_req():
    bucket = Bucket(5, 2)
    for i in range(1, 11):
        print(f'req time: {i}')
        wait_flag = True
        while wait_flag:
            if bucket.consumer():
                print(f'req success: {i}')
                wait_flag = False
            else:
                print(f'Wait token refill')
                time.sleep(1)
                bucket.refill()



if __name__ == '__main__':
    simulate_req()