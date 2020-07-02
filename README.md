# Usage

Just copy those files into your terraform folder.
You can then use ansible (for ad-hoc commands) or ansible-playbook.

# Testing

ansible -m ping all
ansible -m ping masters
ansible -m ping workers

I don't care about other types, feel free to submit a PR to add more groups.
