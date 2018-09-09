#!/usr/bin/env python
from otp import ciphertexts, strxor, KEY_LENGTH

fragments = (
    ' the ',
    ' in order to ',
    ' chipotle',
    ' secret ',
    'the chocolate',
    ' is ',
    'bunnies',
    'death',
)


def is_english(fragment):
    # This is an horrendous cheat, but you can do something that doesn't
    # rely on knowing the plaintexts to know if a given (sub)string is
    # a plausible bit of English
    from otp import messages

    for msg in messages:
        if fragment in msg:
            return True

    return False


if __name__ == "__main__":
    ctexts = ciphertexts()

    for i1 in range(len(ctexts)):
        ctx1 = ctexts[i1]

        for i2 in range(i1+1, len(ctexts)):
            ctx2 = ctexts[i2]
            xord = strxor(ctx1, ctx2)
            matches = []

            for fragment in fragments:
                for position in range(0, len(xord) - len(fragment)):
                    crib = strxor(xord[position:], fragment)
                    if is_english(crib):
#                        print('Found match for "%s" at "%i": "%s"' %
#                              (fragment, position, crib)
#                        )
                        matches += [(position, fragment, crib)]

            if matches:
                # Horrendous cheat again
                # You should be saving the matches across pairs
                # and handle overlapping matches
                matches = sorted(matches, key=lambda (p, _f, _c): p)
                print('Ciphertexts %i and %i' % (i1, i2))
                print('\tMatches:')
                for (position, fragment, crib) in matches:
                    s1 = ('?' * position) + fragment + ('?' * (len(xord) - position - len(fragment)))
                    s2 = ('?' * position) + crib     + ('?' * (len(xord) - position - len(fragment)))
                    print('\t\t%s\n\t\t%s' % (s1, s2))

                print('\tPlaintexts:')
                from otp import messages
                print('\t\t%s\n\t\t%s' % (messages[i1], messages[i2]))
