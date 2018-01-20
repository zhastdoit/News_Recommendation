import './NewsPanel.css';
import _ from 'lodash';

import React from 'react';
import NewsCard from '../NewsCard/NewsCard'

class NewsPanel extends React.Component{
  constructor() {
    super();
    this.state = {news:null}; //Inner variable: news panel has how many news
    this.handleScroll = this.handleScroll.bind(this);
  }

  componentDidMount() { //After constructor finish, run this
    this.loadMoreNews();
    this.loadMoreNews = _.debounce(this.loadMoreNews, 1000);
    window.addEventListener('scroll', this.handleScroll);
  }

  handleScroll() {
    let scrollY = window.scrollY || window.pageYOffset || document.documentElement.scrollTop;
    if ((window.innerHeight + scrollY) >= (document.body.offsetHeight - 50)) {
      console.log('Loading more news');
      this.loadMoreNews();
    }
  }

  loadMoreNews() {
    let request = new Request('http://localhost:3000/news', {
      method: 'GET',
      cache: false});

    fetch(request)
      .then((res) => res.json())
      .then((news) => {
        this.setState({
          news: this.state.news ? this.state.news.concat(news) : news,
        });
      });
  }

  renderNews() {
    //initiallize a function
    let news_list = this.state.news.map(function(news) { //Iteration
      return(
        <a className='list-group-item'>
          <NewsCard news={news} />
        </a>
      );
    });
    //The return for renderNews
    return(  //Render Put the news_list here.
      <div className="container-fluid">
        <div className='list-group'>
          {news_list}
        </div>
      </div>
    );
  }

  render() {
    if (this.state.news) {
        return(
          <div>
            {this.renderNews()}
          </div>
        );
    } else {
      return(
        <div>
          <div id='msg-app-loading'>
            Loading
          </div>
        </div>
      );
    }
  }
}

export default NewsPanel;
