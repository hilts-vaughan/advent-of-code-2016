using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;

namespace AdventDay1
{
    internal class Program
    {
        private const string Input = @"R1, L4, L5, L5, R2, R2, L1, L1, R2, L3, R4, R3, R2, L4, L2, R5, L1, R5, L5, L2, L3, L1, R1, R4, R5, L3, R2, L4, L5, R1, R2, L3, R3, L3, L1, L2, R5, R4, R5, L5, R1, L190, L3, L3, R3, R4, R47, L3, R5, R79, R5, R3, R1, L4, L3, L2, R194, L2, R1, L2, L2, R4, L5, L5, R1, R1, L1, L3, L2, R5, L3, L3, R4, R1, R5, L4, R3, R1, L1, L2, R4, R1, L2, R4, R4, L5, R3, L5, L3, R1, R1, L3, L1, L1, L3, L4, L1, L2, R1, L5, L3, R2, L5, L3, R5, R3, L4, L2, R2, R4, R4, L4, R5, L1, L3, R3, R4, R4, L5, R4, R2, L3, R4, R2, R1, R2, L4, L2, R2, L5, L5, L3, R5, L5, L1, R4, L1, R1, L1, R4, L5, L3, R4, R1, L3, R4, R1, L3, L1, R1, R2, L4, L2, R1, L5, L4, L5";
        // private const string Input = "R8, R4, R4, R8";
        public struct Point
        {
            public int X;
            public int Y ;

            public Point(int x, int y)
            {
                X = x;
                Y = y;
            }

            public override string ToString()
            {
                return $"{X} - {Y}";
            }
        }

        private enum Direction
        {
            North = 0,
            East = 1,
            South = 2,
            West = 3
        }

        public static void Main(string[] args)
        {
            var distances = GetCount();
            Console.WriteLine(distances.Item1);
            Console.WriteLine(distances.Item2);
        }

        static int Mod(int k, int n) {  return ((k %= n) < 0) ? k+n : k;  }

        private static Tuple<int, int> GetCount()
        {
            var start = new Point(0, 0);
            var current = new Point(0, 0);
            var currentDirection = Direction.North;
            var visited = new List<Point> {start};
            var duped = new Point(0, 0);

            var moveCodes = Input.Split(",".ToCharArray(), StringSplitOptions.RemoveEmptyEntries).Select(s => s.Trim());
            foreach (var code in moveCodes)
            {
                var dir = code[0].ToString();
                var wrapAmount = dir == "R" ? 1 : -1;
                currentDirection += wrapAmount;
                currentDirection = (Direction) Mod((int) currentDirection, Enum.GetValues(typeof(Direction)).Length);
                var amount = int.Parse(code.Substring(1).ToString());

                for (var i = 0; i < amount; i++)
                {

                    if (currentDirection == Direction.East)
                        current.X += 1;
                    else if (currentDirection == Direction.West)
                        current.X -= 1;
                    else if (currentDirection == Direction.North)
                        current.Y += 1;
                    else if (currentDirection == Direction.South)
                        current.Y -= 1;


                    if (visited.Contains(current) && duped.Equals(start))
                    {
                        duped = current;
                    }
                    visited.Add(current);

                }
            }

            var x = visited.Contains(new Point(-22, 132));

            // Compute the Taxiderb distance
            var distance = ComputeDistance(start, current);
            var distanceTwice = ComputeDistance(start, duped);
            return Tuple.Create(distance, distanceTwice);
        }

        private static Point FirstDupe(List<Point> visited)
        {
            var firstDupe = new Point(0, 0);
            for (int index = 0; index < visited.Count; index++)
            {
                var p = visited[index];
                for (int i = 0; i < visited.Count; i++)
                {
                    var q = visited[i];

                    if (q.Equals(p) && i != index)
                    {
                        return p;
                    }
                }
            }
            return firstDupe;
        }

        private static int ComputeDistance(Point start, Point current)
        {
            return Math.Abs(start.X - current.X) + Math.Abs(start.Y - current.Y);
        }
    }
}