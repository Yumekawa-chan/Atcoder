n = int(input())
s = []

for i in range(n):
     _ = list(map(int, input().split()))
     s.append(_)

for el in s:
     if "####"or"#.#.##"or"##.#.#"or"#..###"or"##..##"or"###..#"or"##.##"or"#.##.#":
          print("Yes")
          exit()
