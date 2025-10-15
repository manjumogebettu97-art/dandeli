
# Create the complete Apple-style website structure for BookDandeli
# I'll create multiple files: HTML, CSS, and JavaScript

html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BookDandeli - Discover Your Paradise Under the Sky</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <!-- Top Contact Bar -->
    <div class="top-bar">
        <div class="container">
            <div class="contact-info">
                <a href="tel:+917026888000" class="contact-link">
                    <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
                    </svg>
                    +91 7026888000
                </a>
                <a href="mailto:bookdandeli@gmail.com" class="contact-link">
                    <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
                    </svg>
                    bookdandeli@gmail.com
                </a>
            </div>
        </div>
    </div>

    <!-- Sticky Navigation -->
    <nav class="navbar" id="navbar">
        <div class="container">
            <div class="nav-content">
                <a href="#home" class="logo">BookDandeli</a>
                <ul class="nav-links">
                    <li><a href="#home">Home</a></li>
                    <li><a href="#stay">Stay in BookDandeli</a></li>
                    <li><a href="#packages">Packages</a></li>
                    <li><a href="#activities">Adventure Activities</a></li>
                    <li><a href="#contact">Contact Us</a></li>
                    <li><a href="#blog">Blog</a></li>
                </ul>
                <button class="menu-toggle" id="menuToggle">
                    <span></span>
                    <span></span>
                    <span></span>
                </button>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero" id="home">
        <div class="hero-video">
            <div class="hero-overlay"></div>
        </div>
        <div class="hero-content">
            <h1 class="hero-title fade-in">Discover Your Paradise<br>Under the Sky</h1>
            <p class="hero-subtitle fade-in-delay-1">BookDandeli is more than just a getaway; it's a journey into<br>the heart of nature, adventure, and tranquility.</p>
            <a href="#stay" class="cta-button fade-in-delay-2">
                Book Your Adventure Now
                <svg class="arrow-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
                </svg>
            </a>
        </div>
        <div class="scroll-indicator">
            <div class="mouse">
                <div class="wheel"></div>
            </div>
        </div>
    </section>

    <!-- Introduction Section -->
    <section class="intro-section">
        <div class="container">
            <div class="intro-grid">
                <div class="intro-text reveal-left">
                    <h2 class="section-title">Nature's Perfect Escape</h2>
                    <p class="intro-description">
                        Located in the heart of Karnataka, Dandeli is a serene town surrounded by thick forests, 
                        rivers, and a rich wildlife sanctuary. Whether you're seeking peace or adventure, 
                        BookDandeli is the perfect escape from the ordinary.
                    </p>
                    <p class="intro-description">
                        Experience the untouched beauty of Western Ghats, where every moment becomes a memory, 
                        and every adventure tells a story.
                    </p>
                </div>
                <div class="intro-image reveal-right">
                    <div class="image-placeholder">
                        <div class="shimmer"></div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Activities Overview -->
    <section class="activities-section" id="activities">
        <div class="container">
            <h2 class="section-title text-center reveal-up">Adventure Awaits</h2>
            <p class="section-subtitle text-center reveal-up">Explore thrilling activities designed for every adventure enthusiast</p>
            
            <div class="activities-grid">
                <div class="activity-card reveal-up">
                    <div class="activity-icon">
                        <svg viewBox="0 0 64 64" fill="none" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 48c8-8 16-8 24 0s16 8 24 0M12 32l20-16 20 16"/>
                        </svg>
                    </div>
                    <h3>White-Water Rafting</h3>
                    <p>Navigate the thrilling rapids of Kali River on a 12-15 km adventure course</p>
                </div>

                <div class="activity-card reveal-up-delay-1">
                    <div class="activity-icon">
                        <svg viewBox="0 0 64 64" fill="none" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 32c0-8 8-16 16-16s16 8 16 16M32 16v32"/>
                        </svg>
                    </div>
                    <h3>Kayaking</h3>
                    <p>Paddle through serene waters and experience nature up close</p>
                </div>

                <div class="activity-card reveal-up-delay-2">
                    <div class="activity-icon">
                        <svg viewBox="0 0 64 64" fill="none" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 48l24-32 24 32"/>
                        </svg>
                    </div>
                    <h3>Zipline</h3>
                    <p>Fly over dense jungle and take in breathtaking aerial views</p>
                </div>

                <div class="activity-card reveal-up">
                    <div class="activity-icon">
                        <svg viewBox="0 0 64 64" fill="none" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M32 8v48M16 24h32M20 40h24"/>
                        </svg>
                    </div>
                    <h3>Jungle Safari</h3>
                    <p>Explore rich flora and fauna in Dandeli Wildlife Sanctuary</p>
                </div>

                <div class="activity-card reveal-up-delay-1">
                    <div class="activity-icon">
                        <svg viewBox="0 0 64 64" fill="none" stroke="currentColor">
                            <circle cx="32" cy="32" r="16" stroke-width="2"/>
                            <circle cx="32" cy="32" r="8" stroke-width="2"/>
                        </svg>
                    </div>
                    <h3>Zorbing</h3>
                    <p>Roll down hills inside an inflatable ball for ultimate fun</p>
                </div>

                <div class="activity-card reveal-up-delay-2">
                    <div class="activity-icon">
                        <svg viewBox="0 0 64 64" fill="none" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 48l16-24 16 24M24 32h16"/>
                        </svg>
                    </div>
                    <h3>Mountain Biking</h3>
                    <p>Explore rugged terrains and scenic trails through the forest</p>
                </div>

                <div class="activity-card reveal-up">
                    <div class="activity-icon">
                        <svg viewBox="0 0 64 64" fill="none" stroke="currentColor">
                            <ellipse cx="32" cy="32" rx="20" ry="12" stroke-width="2"/>
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 28c4 8 12 8 16 0s12-8 16 0"/>
                        </svg>
                    </div>
                    <h3>Coracle Rides</h3>
                    <p>Traditional round boat rides offering peaceful river exploration</p>
                </div>

                <div class="activity-card reveal-up-delay-1">
                    <div class="activity-icon">
                        <svg viewBox="0 0 64 64" fill="none" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M32 16l-8 8 8 8m0-16l8 8-8 8M20 40h24"/>
                        </svg>
                    </div>
                    <h3>Nature Walks</h3>
                    <p>Tranquil walks perfect for wildlife photography and nature lovers</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Resort Listings -->
    <section class="resorts-section" id="stay">
        <div class="container">
            <h2 class="section-title text-center reveal-up">Stay in BookDandeli</h2>
            <p class="section-subtitle text-center reveal-up">Curated accommodations for every traveler</p>
            
            <div class="resorts-grid">
                <div class="resort-card reveal-scale">
                    <div class="resort-image">
                        <div class="image-placeholder"></div>
                        <div class="resort-badge">Luxury</div>
                    </div>
                    <div class="resort-content">
                        <h3>The Luxury Resort</h3>
                        <p>Premium all-inclusive experience with spa services, gourmet meals, and upscale accommodations</p>
                        <div class="resort-features">
                            <span class="feature-tag">Spa</span>
                            <span class="feature-tag">Fine Dining</span>
                            <span class="feature-tag">Pool</span>
                        </div>
                        <div class="resort-footer">
                            <div class="price-range">
                                <span class="from">From</span>
                                <span class="price">₹5,000</span>
                                <span class="per-night">/night</span>
                            </div>
                            <button class="view-more-btn">
                                View More
                                <svg class="arrow-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
                                </svg>
                            </button>
                        </div>
                    </div>
                </div>

                <div class="resort-card reveal-scale-delay-1">
                    <div class="resort-image">
                        <div class="image-placeholder"></div>
                        <div class="resort-badge">Riverside</div>
                    </div>
                    <div class="resort-content">
                        <h3>The Riverside Resort</h3>
                        <p>Ideal for water sports lovers with rooms overlooking the river and quick access to activities</p>
                        <div class="resort-features">
                            <span class="feature-tag">River View</span>
                            <span class="feature-tag">Water Sports</span>
                            <span class="feature-tag">Cafe</span>
                        </div>
                        <div class="resort-footer">
                            <div class="price-range">
                                <span class="from">From</span>
                                <span class="price">₹3,500</span>
                                <span class="per-night">/night</span>
                            </div>
                            <button class="view-more-btn">
                                View More
                                <svg class="arrow-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
                                </svg>
                            </button>
                        </div>
                    </div>
                </div>

                <div class="resort-card reveal-scale-delay-2">
                    <div class="resort-image">
                        <div class="image-placeholder"></div>
                        <div class="resort-badge">Eco-Friendly</div>
                    </div>
                    <div class="resort-content">
                        <h3>Greenwoods Camp</h3>
                        <p>Perfect for eco-tourism enthusiasts, staying in eco-friendly tents and experiencing nature</p>
                        <div class="resort-features">
                            <span class="feature-tag">Eco Tents</span>
                            <span class="feature-tag">Campfire</span>
                            <span class="feature-tag">Nature</span>
                        </div>
                        <div class="resort-footer">
                            <div class="price-range">
                                <span class="from">From</span>
                                <span class="price">₹2,000</span>
                                <span class="per-night">/night</span>
                            </div>
                            <button class="view-more-btn">
                                View More
                                <svg class="arrow-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
                                </svg>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Travel Info Section -->
    <section class="travel-info-section">
        <div class="container">
            <div class="travel-grid">
                <div class="travel-card reveal-up">
                    <div class="travel-icon">
                        <svg viewBox="0 0 64 64" fill="none" stroke="currentColor">
                            <circle cx="32" cy="32" r="24" stroke-width="2"/>
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M32 12v20l12 8"/>
                        </svg>
                    </div>
                    <h3>Best Time to Visit</h3>
                    <div class="season-info">
                        <div class="season">
                            <strong>Oct - Jan</strong>
                            <p>Cool weather, ideal for outdoor activities</p>
                        </div>
                        <div class="season">
                            <strong>Feb - May</strong>
                            <p>Perfect for adventure activities</p>
                        </div>
                        <div class="season">
                            <strong>Jun - Sep</strong>
                            <p>Monsoon season, lush greenery</p>
                        </div>
                    </div>
                </div>

                <div class="travel-card reveal-up-delay-1">
                    <div class="travel-icon">
                        <svg viewBox="0 0 64 64" fill="none" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 48l20-24 20 24M32 8v16"/>
                        </svg>
                    </div>
                    <h3>How to Reach</h3>
                    <div class="reach-info">
                        <div class="reach-method">
                            <strong>By Train</strong>
                            <p>Dandeli Railway Station via Konkan Railway</p>
                        </div>
                        <div class="reach-method">
                            <strong>By Bus</strong>
                            <p>KSRTC and private buses from nearby cities</p>
                        </div>
                        <div class="reach-method">
                            <strong>By Flight</strong>
                            <p>Hubli Airport, 75 km away</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Activity Details Section -->
    <section class="activity-details-section" id="packages">
        <div class="container">
            <h2 class="section-title text-center reveal-up">Adventure Packages</h2>
            <p class="section-subtitle text-center reveal-up">Detailed activity information and pricing</p>
            
            <div class="activity-details-grid">
                <div class="detail-card reveal-card">
                    <div class="detail-header">
                        <h3>White-Water Rafting</h3>
                        <span class="detail-price">₹2,000<span>/person</span></span>
                    </div>
                    <p>Navigate the thrilling 12-15 km rafting course on Kali River with grade 2 and 3 rapids. Professional guides included. Duration: 2-3 hours.</p>
                    <button class="book-btn">Book Now</button>
                </div>

                <div class="detail-card reveal-card-delay-1">
                    <div class="detail-header">
                        <h3>Jungle Safari</h3>
                        <span class="detail-price">₹1,200<span>/person</span></span>
                    </div>
                    <p>Explore Dandeli Wildlife Sanctuary by jeep. Spot tigers, leopards, elephants, and exotic birds. Safari timings: 6 AM and 4 PM.</p>
                    <button class="book-btn">Book Now</button>
                </div>

                <div class="detail-card reveal-card-delay-2">
                    <div class="detail-header">
                        <h3>Kayaking</h3>
                        <span class="detail-price">₹1,000<span>/person</span></span>
                    </div>
                    <p>Peaceful ride through calm Kali River waters. Safety gear and guide provided. Single or tandem kayak options available.</p>
                    <button class="book-btn">Book Now</button>
                </div>

                <div class="detail-card reveal-card">
                    <div class="detail-header">
                        <h3>Zorbing</h3>
                        <span class="detail-price">₹800<span>/person</span></span>
                    </div>
                    <p>Fun-filled activity rolling down hills in a giant inflatable ball. Suitable for all ages. Experience weightlessness and excitement.</p>
                    <button class="book-btn">Book Now</button>
                </div>

                <div class="detail-card reveal-card-delay-1">
                    <div class="detail-header">
                        <h3>Mountain Biking</h3>
                        <span class="detail-price">₹1,200<span>/person</span></span>
                    </div>
                    <p>Guided mountain biking adventure through scenic trails. Bikes and safety equipment provided. Suitable for beginners and advanced riders.</p>
                    <button class="book-btn">Book Now</button>
                </div>

                <div class="detail-card reveal-card-delay-2">
                    <div class="detail-header">
                        <h3>Zipline</h3>
                        <span class="detail-price">₹1,500<span>/person</span></span>
                    </div>
                    <p>Soar above the jungle canopy on multiple zipline courses. Experience breathtaking views and adrenaline rush. Safety certified.</p>
                    <button class="book-btn">Book Now</button>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section class="contact-section" id="contact">
        <div class="container">
            <h2 class="section-title text-center reveal-up">Get in Touch</h2>
            <p class="section-subtitle text-center reveal-up">Ready to plan your adventure? We're here to help</p>
            
            <div class="contact-grid">
                <div class="contact-form reveal-left">
                    <form id="contactForm">
                        <div class="form-group">
                            <input type="text" placeholder="Your Name" required>
                        </div>
                        <div class="form-group">
                            <input type="email" placeholder="Your Email" required>
                        </div>
                        <div class="form-group">
                            <input type="tel" placeholder="Phone Number" required>
                        </div>
                        <div class="form-group">
                            <select required>
                                <option value="">Select Activity</option>
                                <option value="rafting">White-Water Rafting</option>
                                <option value="safari">Jungle Safari</option>
                                <option value="kayaking">Kayaking</option>
                                <option value="zipline">Zipline</option>
                                <option value="other">Other</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <textarea placeholder="Your Message" rows="4" required></textarea>
                        </div>
                        <button type="submit" class="submit-btn">Send Message</button>
                    </form>
                </div>

                <div class="contact-info-card reveal-right">
                    <div class="info-item">
                        <svg class="info-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
                        </svg>
                        <div>
                            <h4>Phone</h4>
                            <p>+91 7026888000</p>
                        </div>
                    </div>

                    <div class="info-item">
                        <svg class="info-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
                        </svg>
                        <div>
                            <h4>Email</h4>
                            <p>bookdandeli@gmail.com</p>
                        </div>
                    </div>

                    <div class="info-item">
                        <svg class="info-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
                        </svg>
                        <div>
                            <h4>Address</h4>
                            <p>State Adventure Opp. Bus Stand<br>J.N. Road, Dandeli</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Blog Section -->
    <section class="blog-section" id="blog">
        <div class="container">
            <h2 class="section-title text-center reveal-up">Latest from Our Blog</h2>
            <p class="section-subtitle text-center reveal-up">Insights, tips, and guides for your Dandeli adventure</p>
            
            <div class="blog-grid">
                <div class="blog-card reveal-scale">
                    <div class="blog-image">
                        <div class="image-placeholder"></div>
                    </div>
                    <div class="blog-content">
                        <span class="blog-category">Travel Guide</span>
                        <h3>Dandeli's Hidden Gems</h3>
                        <p>Explore off-the-beaten-path locations in Dandeli that most tourists miss. Discover secret waterfalls and serene spots.</p>
                        <a href="#" class="read-more">Read More →</a>
                    </div>
                </div>

                <div class="blog-card reveal-scale-delay-1">
                    <div class="blog-image">
                        <div class="image-placeholder"></div>
                    </div>
                    <div class="blog-content">
                        <span class="blog-category">Adventure</span>
                        <h3>Adventure Activities Guide</h3>
                        <p>Detailed guides on all adventure activities, their benefits, safety measures, and what to expect during your visit.</p>
                        <a href="#" class="read-more">Read More →</a>
                    </div>
                </div>

                <div class="blog-card reveal-scale-delay-2">
                    <div class="blog-image">
                        <div class="image-placeholder"></div>
                    </div>
                    <div class="blog-content">
                        <span class="blog-category">Family</span>
                        <h3>Family Fun at BookDandeli</h3>
                        <p>The perfect vacation options for families, including kid-friendly activities, family packages, and accommodation tips.</p>
                        <a href="#" class="read-more">Read More →</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col">
                    <h3 class="footer-title">BookDandeli</h3>
                    <p class="footer-description">Your gateway to nature, adventure, and unforgettable experiences in the heart of Karnataka.</p>
                    <div class="social-links">
                        <a href="#" class="social-link" aria-label="Instagram">
                            <svg viewBox="0 0 24 24" fill="currentColor">
                                <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
                            </svg>
                        </a>
                        <a href="#" class="social-link" aria-label="Facebook">
                            <svg viewBox="0 0 24 24" fill="currentColor">
                                <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>
                            </svg>
                        </a>
                        <a href="#" class="social-link" aria-label="Twitter">
                            <svg viewBox="0 0 24 24" fill="currentColor">
                                <path d="M23.953 4.57a10 10 0 01-2.825.775 4.958 4.958 0 002.163-2.723c-.951.555-2.005.959-3.127 1.184a4.92 4.92 0 00-8.384 4.482C7.69 8.095 4.067 6.13 1.64 3.162a4.822 4.822 0 00-.666 2.475c0 1.71.87 3.213 2.188 4.096a4.904 4.904 0 01-2.228-.616v.06a4.923 4.923 0 003.946 4.827 4.996 4.996 0 01-2.212.085 4.936 4.936 0 004.604 3.417 9.867 9.867 0 01-6.102 2.105c-.39 0-.779-.023-1.17-.067a13.995 13.995 0 007.557 2.209c9.053 0 13.998-7.496 13.998-13.985 0-.21 0-.42-.015-.63A9.935 9.935 0 0024 4.59z"/>
                            </svg>
                        </a>
                    </div>
                </div>

                <div class="footer-col">
                    <h4 class="footer-heading">Quick Links</h4>
                    <ul class="footer-links">
                        <li><a href="#home">Home</a></li>
                        <li><a href="#stay">Stay in BookDandeli</a></li>
                        <li><a href="#packages">Packages</a></li>
                        <li><a href="#activities">Adventure Activities</a></li>
                    </ul>
                </div>

                <div class="footer-col">
                    <h4 class="footer-heading">Support</h4>
                    <ul class="footer-links">
                        <li><a href="#contact">Contact</a></li>
                        <li><a href="#blog">Blog</a></li>
                        <li><a href="#">FAQs</a></li>
                        <li><a href="#">Terms & Conditions</a></li>
                    </ul>
                </div>

                <div class="footer-col">
                    <h4 class="footer-heading">Contact Info</h4>
                    <ul class="footer-contact">
                        <li>+91 7026888000</li>
                        <li>bookdandeli@gmail.com</li>
                        <li>State Adventure Opp. Bus Stand<br>J.N. Road, Dandeli</li>
                    </ul>
                </div>
            </div>

            <div class="footer-bottom">
                <p>&copy; 2025 BookDandeli. All rights reserved. Crafted with passion for adventure.</p>
            </div>
        </div>
    </footer>

    <script src="script.js"></script>
</body>
</html>'''

# Save HTML file
with open('bookdandeli.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ HTML file created: bookdandeli.html")
print("File size:", len(html_content), "bytes")
