from distutils.core import setup
setup(
  name = 'lingfeat',
  packages = ['lingfeat'],
  version = '0.1.0',
  license='cc-by-sa-4.0',
  description = 'Comprehensive Linguistic Features Extraction for Readability Assessment', 
  author = 'Bruce W. Lee',        
  author_email = 'phys.w.s.lee@gmail.com', 
  url = 'https://github.com/brucewlee',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # Not released yet
  keywords = ['NLP', 'FEATURE EXTRACTION', 'READABILITY'], 
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: Creative Commons Attribution Share Alike 4.0',   # Again, pick a license
    'Programming Language :: Python :: 3.6',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)