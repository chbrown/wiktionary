## Wiktionary tools

Right now there's basically one feature, an etymology extractor.
    
Get an English Wiktionary dump, e.g.,
    
    export CORPORA=~/corpora
    mkdir -p $CORPORA/wiktionary
    cd $CORPORA/wiktionary
    wget http://dumps.wikimedia.org/enwiktionary/20130503/enwiktionary-20130503-pages-articles-multistream.xml.bz2
    bunzip2 enwiktionary-20130503-pages-articles-multistream.xml.bz2
    # make sure we're good:
    ls -la $CORPORA/wiktionary/enwiktionary-20130503-pages-articles-multistream.xml
    # cool

Then run the etymology extractor.
      
    git clone git://github.com/chbrown/wiktionary.git wiktionary-dev
    cd wiktionary-dev
    python setup.py develop
    cd wiktionary
    python etymology.py
    
It'll parse through the 147,095 entries that have etymologies in about five minutes.
