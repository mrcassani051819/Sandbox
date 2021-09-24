using System;
using System.Collections.Generic;

namespace SuspiciousTransactions
{
    class LogParser
    {
        public SortedList<string, int> countUserTransactions(List<string> logs)
        {
            SortedList<string, int> userTransactions = new SortedList<string, int>();
            foreach (string entry in logs)
            {
                string[] transaction = entry.Split(' ');
                string payer = transaction[0];
                string payee = transaction[1];
                // ignoring amount
                if (payer != payee) {
                    if (!userTransactions.ContainsKey(payer)) {
                        userTransactions.Add(payer, 1);
                    } else {
                        userTransactions[payer] += 1;
                    }
                    if (!userTransactions.ContainsKey(payee)) {
                        userTransactions.Add(payee, 1);
                    } else {
                        userTransactions[payee] += 1;
                    }
                } else {
                    if (!userTransactions.ContainsKey(payer)) {
                        userTransactions.Add(payer, 1);
                    } else {
                        userTransactions[payer] += 1;
                    }
                }
            }
            return userTransactions;
        }

        public List<string> findSuspiciousTransactors(SortedList<string, int> transactions, int threshold)
        {
            List<string> suspiciousTransactions = new List<string>();
            foreach(string userID in transactions.Keys)
            {
                if (transactions[userID] >= threshold) {
                    suspiciousTransactions.Add(userID);
                }
            }
            suspiciousTransactions.Sort();
            return suspiciousTransactions;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            List<string> logs = new List<string>();
            logs.Add("24 32 1");
            logs.Add("12 24 1");
            logs.Add("12 12 1");
            LogParser p = new LogParser();
            SortedList<string, int> result = p.countUserTransactions(logs);
            // Use to check if totals are correct.
            // foreach (string userID in result.Keys)
            // {
            //     Console.WriteLine(userID + " " + result[userID]);
            // }
            List<string> suspicious = p.findSuspiciousTransactors(result, 2);
            // Print out the results.
            foreach (string entry in suspicious)
            {
                Console.WriteLine(entry);
            }
        }
    }
}
