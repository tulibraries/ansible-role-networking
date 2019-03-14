TU Libraries Ansible Role for Networking
=========

This is a role to overlay application- or subsystem-specific networking rules.

It is applied to specific infrastructure via Playbook's use of hosts with the role's invocation.

Requirements
------------

Use `Pipenv` and `.python-version` files to know the required libraries to run this role.

Role Variables
--------------

- `trusted_sources`: list of IPs that you want to enable access over the trusted firewalld zone.
- `trusted_services`: list of defined services you want to enable for the trusted firewalld zone.
- `public_services`: list of defined services you want to enable for the public firewalld zone.


Dependencies
------------

This role requires no other roles or libraries. It works through the `firewalld` ansible module.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: networking, x: 42 }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a
website (HTML is not allowed).
