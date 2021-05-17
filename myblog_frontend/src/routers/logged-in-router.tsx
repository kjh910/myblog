import React from 'react';
import { BrowserRouter as Router} from "react-router-dom";
import { Header } from '../components/header';
import { Main } from '../pages/main';
import { Footer } from '../pages/footer';
import { NavBar } from '../components/navBar';
import { ContentList } from '../pages/contentList';

export const LoggedInRouter = () => {
    return (
        <Router>
            <Header />
            <div className="container w-full md:max-w-5xl mx-auto pt-20">
                <div className="grid grid-cols-2 md:grid-cols-3">
                    <div className="col-span-2">
                        <ContentList />
                        <Main />
                    </div>
                    <div>
                        <NavBar />
                    </div>
                </div>
            </div>
            <Footer />
        </Router>
        
    );
}