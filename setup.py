from distutils.core import setup
setup(
  name = 'google_ngram_api',         
  packages = ['google_ngram_api'],   
  version = '1.2',      
  license='MIT',        
  description = 'API to download google ngram data as csv file',   
  author = 'Venkatesh Prasad',                   
  author_email = 'prasad.venkatesh90@gmail.com',      
  url = 'https://github.com/prasa-dd-vp/google_ngram_api',   
  download_url = 'https://github.com/prasa-dd-vp/google_ngram_api/archive/v_01.tar.gz',    
  keywords = ['google', 'googlengram', 'api', 'csvdownloader', 'ngramdata', 'googledata', 'csv', 'downlader'],   
  install_requires=[            
          'pandas',
          'requests',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)