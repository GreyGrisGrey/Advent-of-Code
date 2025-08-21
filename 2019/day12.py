from math import gcd

def moonString(moons, vels, index):
    newString = ""
    for i in range(len(moons)):
        newString += str(moons[i][index]) + ":"
        newString += str(vels[i][index]) + ":"
    return newString

def partBoth(fileName = "in.txt"):
    data = open(fileName).read().split("\n")
    moons = []
    vels = []
    caches = [{}, {}, {}]
    nums = [0, 0, 0]
    steps = 0
    for i in data:
        moons.append(list(map(lambda num: int(num.split("=")[1]), i.strip("<>").split(", "))))
        vels.append([0, 0, 0])
    for i in range(4686774924):
        if nums[2] != 0 and nums[1] != 0 and nums[0] != 0:
            break
        if steps == 1000:
            total = 0
            for i in range(len(moons)):
                news = [0, 0]
                for j in range(3):
                    news[0] += abs(moons[i][j])
                    news[1] += abs(vels[i][j])
                total += news[0] * news[1]
            print("Part 1:", total)
        if i % 500000 == 0:
            print(i)
        for j in range(len(moons)):
            for k in range(len(moons)):
                if j < k:
                    for l in range(3):
                        if moons[j][l] > moons[k][l]:
                            vels[j][l] -= 1
                            vels[k][l] += 1
                        elif moons[j][l] < moons[k][l]:
                            vels[j][l] += 1
                            vels[k][l] -= 1
        for j in range(len(moons)):
            for k in range(3):
                moons[j][k] += vels[j][k]
        steps += 1
        caches[0][moonString(moons, vels, 0)] = True
        caches[1][moonString(moons, vels, 1)] = True
        caches[2][moonString(moons, vels, 2)] = True
        if len(caches[0]) != steps and nums[0] == 0:
            nums[0] = steps - 1
        if len(caches[1]) != steps and nums[1] == 0:
            nums[1] = steps - 1
        if len(caches[2]) != steps and nums[2] == 0:
            nums[2] = steps - 1
    curr = nums[0]
    curr = int(curr * nums[1] / gcd(nums[1], nums[0]))
    curr = curr * nums[2] / gcd(nums[2], curr)
    print("Part 2:", int(curr))

if __name__ == "__main__":
    partBoth("in12.txt")