import re

# Space : O(n)
# Time  : O(n)


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        mailmap = {}

        for mail in emails:
            local, domain = mail.split('@')

            # clean local
            local = local.split('+')[0]
            local = "".join(re.findall(r'[^\.]+', local))

            if (local + '@' + domain) not in mailmap:
                mailmap[(local + '@' + domain)] = 1
            else:
                mailmap[(local + '@' + domain)] += 1

        return len(mailmap)
