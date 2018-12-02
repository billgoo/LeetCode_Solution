class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        email_set = set()
        for email in emails:
            local, _, domain = email.partition("@")
            if '+' in local:
                local = local[:local.index('+')]
            local = local.replace('.', '')
            email_set.add(local + "@" + domain)
        return len(email_set)